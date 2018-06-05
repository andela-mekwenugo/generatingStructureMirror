class GenerateStructure(object):

    def __init__(self, ad_group_id=None, criterion_id=None, bid_modifier=None):
        self.ad_group_id = ad_group_id
        self.criterion_id = criterion_id
        self.bid_modifier = bid_modifier

    def _get_base_operation(self, operator, operand):
        operations_base = {
            'operator': operator,
            'operand': operand
        }
        return operations_base

    def case1_ad_group_bid(self, action):
        ad_group_bid_operand = {
            'adGroupId': self.ad_group_id,
            'criterion': {
                'xsi_type': 'Platform',
                'id': self.criterion_id
            },
            'bidModifier': self.bid_modifier
        }

        operations = self._get_base_operation(action, ad_group_bid_operand)

        return operations

    def _generate_key_word(self, xsi_type, criterion_xsi_type, matchType, text):
        keyword = {
            'xsi_type': xsi_type,
            'adGroupId': self.ad_group_id,
            'criterion': {
                'xsi_type': criterion_xsi_type,
                'matchType': matchType,
                'text': text
            }
        }
        return keyword

    def case2_ad_group_criterion(self, action, args=None):
        keyword_list = []
        operation_list = []
        if args is None:
            args = []
        num_of_args = len(args)
        if num_of_args >= 1:
            for item in args:
                keyword_list.append(self._generate_key_word(item[0], item[1], item[2], item[3]))
        for num in range(num_of_args):
            operation_list.append(self._get_base_operation(action, keyword_list[num]))
        return operation_list

    def case3_pause_campaigns(self, action, campaign_id):
        pause_campaign_operande = {
            'id': campaign_id,
            'status': 'PAUSED'
        }
        operations = self._get_base_operation(action, pause_campaign_operande)

        return operations
