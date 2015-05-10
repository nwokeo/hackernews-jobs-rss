import datetime
import PyRSS2Gen
import urllib2
import json

def buildXML():
    jobIds = json.loads(urllib2.urlopen('https://hacker-news.firebaseio.com/v0/jobstories.json').read())
    items = []
    for jobId in jobIds:
        jobUrl = 'https://hacker-news.firebaseio.com/v0/item/' + str(jobId) + '.json?print=pretty'
        jobData = json.loads(urllib2.urlopen(jobUrl).read())
        items.append(PyRSS2Gen.RSSItem(
             title = jobData['title'],
             link = jobData['url'],
             description = jobData['text'],
             guid = str(jobData['id']),
             pubDate = datetime.datetime.fromtimestamp(int(jobData['time'])).strftime('%Y-%m-%d %H:%M:%S')
             ))
    writeXML(items)

def writeXML(items):            
    rss = PyRSS2Gen.RSS2(
        title = "HackerNews Generated Jobs Feed",
        link = "https://news.ycombinator.com/jobs",
        description = "These are jobs at startups that were funded by Y Combinator. Some are now established companies; others may only be a few weeks old.",
        lastBuildDate = datetime.datetime.now(),
        items = items)
    
    rss.write_xml(open("public/hackerNewsJobsRss.xml", "w"))

if __name__ == "__main__":
    buildXML()