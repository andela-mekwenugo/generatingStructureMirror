# # Create operations

# Most of the time our code is supposed to support marketing operations on their daily work,
# e.g. by handling change management in a programmatic way.
# 
# Among others we have to programmatically:
# - handle bidding changes for all the keywords in our portfolio
# - automatically create new keywords
# - pause entire campaigns
# 
# Fortunately Google Adwords offers us a well developed API do that.
# 
# All above bullet points are so called operations that we can pass as an object to an instance of 
# a certain google adwords service. In the follwoing cases you can find some examples for the services and objects.

# ### Case 1

# the following snipped shows an operation to add a bid modifier on adgroup level

ad_group_bid_modifier_service = client.GetService('AdGroupBidModifierService', version='v201710')

adgoup_id = 1234
criterion_id = 4321
bid_modifier = 1.1

operation = {
  # Use 'ADD' to add a new modifier
  'operator': 'ADD',
  'operand': {
      'adGroupId': ad_group_id,
      'criterion': {
          'xsi_type': 'Platform',
          'id': criterion_id
      },
      'bidModifier': bid_modifier
  }
}

ad_group_bid_modifier_service.mutate([operation])


# ### Case 2

# The following snipped shows an operation to add keywords

ad_group_criterion_service = client.GetService(
  'AdGroupCriterionService', version='v201710')

# Construct keyword ad group criterion objects.
keyword1 = {
  'xsi_type': 'BiddableAdGroupCriterion',
  'adGroupId': ad_group_id,
  'criterion': {
      'xsi_type': 'Keyword',
      'matchType': 'BROAD',
      'text': 'mars'
  },
}

keyword2 = {
  'xsi_type': 'NegativeAdGroupCriterion',
  'adGroupId': ad_group_id,
  'criterion': {
      'xsi_type': 'Keyword',
      'matchType': 'EXACT',
      'text': 'pluto'
  }
}

# Construct operations and add ad group criteria.
operations = [
  {
      'operator': 'ADD',
      'operand': keyword1
  },
  {
      'operator': 'ADD',
      'operand': keyword2
  }
]

ad_group_criteria = ad_group_criterion_service.mutate(
operations)['value']


# ### Case 3

# The following snipped shows an operation to pause a campaign

campaign_service = client.GetService('CampaignService', version='v201710')

# Construct operations and pause campaign.
operations = [{
  'operator': 'SET',
  'operand': {
      'id': campaign_id,
      'status': 'PAUSED'
  }
}]

campaign_service.mutate(operations)


# 
# ## Assignment:
# 
# Since all of those operations follow a common structure, we want you to create generalized 
# methods organized in a class that help us generating structure and content of those operations 
# based on the desired business case (changing bid modifiers, adding keywords, pausing campaigns)
# 
# Make sure that all methods are tested and easy to read
