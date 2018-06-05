import unittest
from generate import GenerateStructure


class GenerateStructureTest(unittest.TestCase):
    def setUp(self):
        self.gs = GenerateStructure(ad_group_id=23, criterion_id=34, bid_modifier=1.1)

    def test_get_base_operation(self):
        test_operand = {'adGroupId': 11}
        base_operation = self.gs._get_base_operation('ADD', test_operand)
        self.assertEqual(base_operation, {'operator': 'ADD', 'operand': {'adGroupId': 11}})

    def test_ad_group_bid(self):
        group_bid_operation = self.gs.case1_ad_group_bid(action='ADD')
        expected_output = {
            'operator': 'ADD',
            'operand': {
                'adGroupId': 23,
                'criterion': {'xsi_type': 'Platform', 'id': 34},
                'bidModifier': 1.1
            }
        }
        self.assertEqual(group_bid_operation, expected_output)

    def test_generate_key_word(self):
        k_word = self.gs._generate_key_word('BiddableAdGroupCriterion', 'keyword', 'BROAD', 'mars')
        self.assertEqual(k_word, {
            'xsi_type': 'BiddableAdGroupCriterion',
            'adGroupId': 23,
            'criterion': {
                'xsi_type': 'keyword',
                'matchType': 'BROAD',
                'text': 'mars'
            }
        })

    def test_case2_ad_group_criterion(self):
        args = [['BiddableAdGroupCriterion', 'Keyword', 'BROAD', 'mars'], ['NegativeAdGroupCriterion', 'Keyword', 'EXACT', 'pluto']]
        expected_output = [
            {
                'operator': 'ADD',
                'operand': {
                    'xsi_type': 'BiddableAdGroupCriterion',
                    'adGroupId': 23,
                    'criterion': {'xsi_type': 'Keyword', 'matchType': 'BROAD', 'text': 'mars'}
                }
            },
            {
                'operator': 'ADD',
                'operand': {
                    'xsi_type': 'NegativeAdGroupCriterion',
                    'adGroupId': 23,
                    'criterion': {'xsi_type': 'Keyword', 'matchType': 'EXACT', 'text': 'pluto'}
                }
            }]
        self.assertEqual(self.gs.case2_ad_group_criterion(action='ADD', args=args), expected_output)

    def test_case3_pause_campaigns(self):
        pause_campaign = self.gs.case3_pause_campaigns(action='SET', campaign_id=90)
        expected_output = {'operator': 'SET', 'operand': {'id': 90, 'status': 'PAUSED'}}
        self.assertEqual(pause_campaign, expected_output)

if __name__ == '__main__':
    unittest.main()
