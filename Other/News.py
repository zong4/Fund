from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='9a2364318a4743c6a3edb62f6589bbbf')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(
                                          # q='China',
                                          # sources='bbc-news,the-verge',
                                          category='general',
                                          language='zh',
                                          )

# /v2/everything
# all_articles = newsapi.get_everything(q='bitcoin',
#                                       sources='bbc-news,the-verge',
#                                       domains='bbc.co.uk,techcrunch.com',
#                                       from_param='2017-12-01',
#                                       to='2017-12-12',
#                                       language='en',
#                                       sort_by='relevancy',
#                                       page=2)

# /v2/top-headlines/sources
newsapi.get_sources()

# for top_headline in top_headlines['articles']:
#     print(top_headline['title'],'time:',top_headline['publishedAt'])

