#!/usr/bin/python3

from es_tutorial.py import upload

def test_upload():
    assert upload("~/Downloads/shakespear_2.json") == {"_index": "shakespeare",
                    "_type": "doc",
                    "_source": {
                        "speaker": d["speaker"],
                        "play_name": d["play_name"],
                        "line_id": d["line_id"],
                        "speech_number": d["speech_number"]
                        } 
                    })
