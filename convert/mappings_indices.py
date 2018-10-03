#!/usr/bin/python3

''' Truncated Class of Mappings, and Indices used for elasticsearch ingestion'''
 
class Mappings:
    # mappings for elasticsearch indices  
    def __init__(self): 
        self.posts = """{
            "mappings": {
                "posts": {
                    "properties": {
                        "@Id": {"type": "integer"},
                        "@Score": {"type": "integer"},
                        "@ViewCount": {"type": "integer"},
                        "@Body": {"type": "text"},
                        "@AnswerCount": {"type": "integer"},
                        "@CommentCount": {"type": "integer"}
                    }
                }
            }
        }"""
        self.comments =  """{
            "mappings": {
                "comments": {
                    "properties": {               
                        "@Id": {"type": "integer"},
                        "@PostId": {"type": "integer"},
                        "@Score": {"type": "integer"},
                        "@Text": {"type": "text"}
                    }
                }
            }
        }"""

class Indices():
    # dictionaries for elasticsearch bulk load
    def posts(self, review):
        return {
            "_index": "posts",
            "_type": "posts",
            "_source": {
                "@Id": review.get("@Id", None),
                "@Score": review.get("@Score", None),
                "@ViewCount": review.get("@ViewCount", None),
                "@Body": review.get("@Body", None),
                "@AnswerCount": review.get("@AnswerCount", None),
                "@CommentCount": review.get("@CommentCount", None)
            }
        }
    
    def comments(self, review):
        return {
            "_index": "comments",
            "_type": "review",
            "_source": {
            "@Id": review["@Id"],
            "@PostId": review["@PostId"],
            "@Score": review["@Score"],
            "@Text": review["@Text"]
            }
        }