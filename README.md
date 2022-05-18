# ShIssueNews
To uncover the relationship of the characters appearing in the series of new issue in shanghai government offical website.

## Collect 
>  https://www.shanghai.gov.cn/nw4411....
>  wechat public account (this is pretty hard since the api is not quite clear to me right now)

scrapy crawl shi -o items.json -s FEED_EXPORT_ENCODING='utf-8'
OR
scrapy crawl shi 

the code can transfer the scraped data to mongodb as well as local file.

mongodb should be turned on before everything.

The scraped json data will be transferred to filcease ANALYSIS for further analysis.

## Analysis (of semantics)
>  characters-word
>  word splitting
>  their relation

## Display
>> word cloud 
>> appearing frequency
>> verbs that appeared
>> graph linking all the people with weight of closeness
>> the automatic generation of similar text shit.