from mrjob.job import MRJob
from mrjob.protocol import JSONValueProtocol
import itertools

class UserSimilarity(MRJob):
    INPUT_PROTOCOL = JSONValueProtocol

    ###
    # TODO: write the functions needed to
    # 1) find potential matches, 
    # 2) calculate the Jaccard between users, with a user defined as a set of
    # reviewed businesses
    ##/
    def get_user(self, _,record):
        if record['type'] == 'review':
            yield (record['user_id'], record['business_id'])

    def red_user_business(self, user, business):
        yield [user, list(business)]

    def map_users (self, user, businesses):
            yield ["user", [user, businesses]]

    #def reduce_pairs (self, user, user_info):
     #   yield [[user, user], [user_info, user_info]]

    def calc_simularity (self, user, user_info):
        pairs = list(itertools.combinations(list(user_info),2))
        for pair_info in pairs:
            sim = len(list(set(pair_info[0][1]) & set(pair_info[1][1])))
            jac = sim/(len(pair_info[0][1]) + len(pair_info[1][1]))
            if (jac >= 0.5):
                yield [[pair_info[0][0], pair_info[1][0]], jac]


    def steps(self):
        """TODO: Document what you expect each mapper and reducer to produce:
        mapper1: <line, record> => <key, value>
        reducer1: <key, [values]>
        mapper2: ...
        """
        return [self.mr(mapper=self.get_user, reducer=self.red_user_business),
        self.mr(mapper=self.map_users, reducer=self.calc_simularity)]


if __name__ == '__main__':
    UserSimilarity.run()
