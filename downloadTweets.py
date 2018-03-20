#Import the necessary methods from tweepy library
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import datetime
import smtplib

#Variables that contains the user credentials to access Twitter API 
access_token = "<access_token>"
access_token_secret = "<access_token_secret>"
consumer_key = "<consumer_key>"
consumer_secret = "<consumer_secret>"

Twitter_Keywords=['e-cig','ecig','e-cigs','ecigs','e-cigarette','ecigarette','e-cigarettes','ecigarettes','vape','vaper','vaping','vapes','vapers','nicotine','tobacco','cigarette','cigarettes','cigar','atomizer','atomizers','cartomizer','cartomizers','ehookah','e-hookah','ejuice','ejuices','e-juice','e-juices','eliquid','eliquids','e-liquid','e-liquids','blu','njoy','green smoke','south beach smoke','eversmoke','joye 510','joye510','joyetech','lavatube','lavatubes','logicecig','logicecigs','smartsmoker','smokestiks','v2 cig','v2 cigs','v2cigs','v2cig','mistic','21st century smoke','logic black label','finiti','nicotek','cigirex','logic platinum','cigalectric','xhale o2','cig2o','green smart living','krave','secondhand vape','secondhand vaping','second-hand vape','second-hand vaping','vape smoke','ecig smoke','e-cig smoke','e-cigarette smoke','vape shs','ecig shs','vape secondhand smoke','vape second-hand smoke','esmoke','e-smoke','stillblowingsmoke','still blowing smoke','notblowingsmoke','not blowing smoke','capublichealth','tobaccofreekids','notareplacement','trulyfree','truly free','sb140','sb 140','sb24','sb 24','cherry tip cigarillos','mini-cigarillos','tip cigarillos','king edward cigars','royal gold cigars','sweet coronella','swisher blk','swisher sweets','vapercon','vapercon west','grimmgreen','vapor','electronic cigarette','vape meet','EcigsSaveLive','EcigsSaveLives','EcigsSavesLives']


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        fileName="/home/isi/data/sree/data/"+datetime.date.today().strftime ("%m-%d-%Y")+".json";
        #fileName=datetime.date.today().strftime ("%m-%d-%Y")+".json"
        #print(fileName)
        with open(fileName,'a') as tf:
            tf.write(data)
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    try:
    	stream.filter(track=Twitter_Keywords,languages=["en"])
    except:
    	server = smtplib.SMTP('smtp.gmail.com', 587)
    	server.starttls()
    	server.login("EMAIL ID", "PASSWORD")
 
    	msg = "Program came to an end! Its from the HPC"
    	server.sendmail("FROM EMAIL ID", "EMAIL ID TO BE ALERTED WHEN DATA COLLLECTION FAILS", msg)
	server.sendmail("FROM EMAIL ID","EMAIL ID TO BE ALERTED WHEN DATA COLLECTION FAILS",msg)
    	server.quit()
