# 29f4d981bb9d4e2cbfe32bc2fd8a416d
# GET https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=29f4d981bb9d4e2cbfe32bc2fd8a416d
# importing requests package
# import requests	 

# def NewsFromBBC():
	
# 	# BBC news api
# 	# following query parameters are used
# 	# source, sortBy and apiKey
# 	query_params = {
# 	"source": "bbc-news",
# 	"sortBy": "top",
# 	"apiKey": "29f4d981bb9d4e2cbfe32bc2fd8a416d"
# 	}
# 	main_url = " https://newsapi.org/v1/articles"

# 	# fetching data in json format
# 	res = requests.get(main_url, params=query_params)
# 	open_bbc_page = res.json()

# 	# getting all articles in a string article
# 	article = open_bbc_page["articles"]

# 	# empty list which will 
# 	# contain all trending news
# 	results = []
	
# 	for ar in article:
# 		results.append(ar["title"])
		
# 	for i in range(len(results)):
		
# 		# printing all trending news
# 		print(i + 1, results[i])

# 	#to read the news out loud for us
# 	from win32com.client import Dispatch
# 	speak = Dispatch("SAPI.Spvoice")
# 	speak.Speak(results)				 

# # Driver Code
# if __name__ == '__main__':
	
# 	# function call
# 	NewsFromBBC() 

import requests

def newsFromBBC():
    query_params={
        "source":"bbc-news",
        "sortBy":"top",
        "apiKey":"29f4d981bb9d4e2cbfe32bc2fd8a416d"
    }
    main_url="https://newsapi.org/v1/articles"
    res=requests.get(main_url,params=query_params)
    open_bbc_page=res.json()
    
    article=open_bbc_page["articles"]
    result = []
    for ar in article:
        result.append(f"title: {ar['title']}: description: {ar['description']}")

    from win32com.client import Dispatch
    speak=Dispatch("SAPI.Spvoice")
    
    for i in range(len(result)):
        print(i+1,result[i])
        speak.Speak(result[i])

if __name__=="__main__":
    newsFromBBC()