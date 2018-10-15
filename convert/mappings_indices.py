#!/usr/bin/python3

'''Truncated Class of Mappings, and Indices used for elasticsearch ingestion'''
 
class Mappings:
    # mappings for elasticsearch indices  
    def __init__(self): 
        self.posts = """{
            "mappings": {
                "posts": {
                    "properties": {
                        "Id": {"type": "integer"},
                        "Score": {"type": "integer"},
                        "ViewCount": {"type": "integer"},
                        "Body": {"type": "text"},
                        "AnswerCount": {"type": "integer"},
                        "CommentCount": {"type": "integer"}
                    }
                }
            }
        }"""
        # A post is either an accepted answer or question.  The question
        # may have an accepted answer designated with the keyword 
        # "AcceptedAnswerId" or the accepted answer may be due to its
        # "Score." 
        self.posts2 = """{
            "mappings": {
                "posts2": {
                    "properties": {
                        "Id": {"type": "keyword"},
                        "Score": {"type": "integer"},
                        "Body": {"type": "text"},
                        "ParentId": {"type": "keyword"},
                        "AcceptedAnswerId": {"type": "keyword"}
                    }
                }
            }
        }"""
        self.comments =  """{
            "mappings": {
                "comments": {
                    "properties": {               
                        "Id": {"type": "integer"},
                        "PostId": {"type": "integer"},
                        "Score": {"type": "integer"},
                        "Text": {"type": "text"}
                    }
                }
            }
        }"""
        self.postlinks =  """{
            "mappings": {
                "postlinks": {
                    "properties": {               
                        "Id": {"type": "integer"},
                        "CreationDate": {"type": "date"}
                        "PostId": {"type": "integer"},
                        "RelatedPostId": {"type": "integer"},
                        "LinkTypeId": {"type": "integer"}
                    }
                }
            }
        }"""
        self.badges = """{
           "mappings": {
                "badges": {
                    "properties": {               
                        "Id": {"type": "integer"},
                        "UserId": {"type": "integer"}
                        "Name": {"type": "integer"},
                        "Date": {"type": "date"},
                        "Class": {"type": "integer"},
                        "TagBased": {"type": boolean}
                    }
                }
            }
        }"""

class Indices():
    # dictionaries for elasticsearch bulkload
    def posts(self, review):
        return {
            "_index": "posts",
            "_type": "posts",
            "_source": {
                "Id": review.get("Id", None),
                "Score": review.get("Score", None),
                "ViewCount": review.get("ViewCount", None),
                "Body": review.get("Body", None),
                "AnswerCount": review.get("AnswerCount", None),
                "CommentCount": review.get("CommentCount", None)
            }
        }
    def posts2(self, review):
        return {
            "_index": "posts2",
            "_type": "posts2",
            "_source": {
                "Id": review.get("Id", None),
                "Score": review.get("Score", None),
                "ParentId": review.get("ParentId", None),
                "Body": review.get("Body", None),
                "AcceptedAnswerId": review.get("AcceptedAnswerId", None)
            }
        }
    def comments(self, review):
        return {
            "_index": "comments",
            "_type": "review",
            "_source": {
                "Id": review["Id"],
                "PostId": review["PostId"],
                "Score": review["Score"],
                "Text": review["Text"]
            }
        }

    def postlinks(self, review): 
        return {
            "_index": "postlinks",
            "_type": "review",
            "_source": {
                "Id": review.get("Id", None),
                "CreationDate": review.get("CreationDate", None),
                "PostId": review.get("PostId", None),
                "RelatedPostId": review.get("RelatedPostId", None), 
                "LinkTypeId": review.get("LinkTypeId", None)
            }
        }

    def badges(self, review): 
        return {
            "_index": "badges",
            "_type": "review",
            "_source": {
                "Id": review.get("Id", None),
                "UserId": review.get("UserId", None),
                "Name": review.get("Name", None),
                "Date": review.get("Date", None),
                "Class": review.get("Class", None),
                "TagBased": review.get("TagBased", None)
            }
        }