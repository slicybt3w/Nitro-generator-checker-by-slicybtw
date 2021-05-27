from flask import Flask

from threading import Thread
app = Flask('app')

@app.route('/')
def slicy():
  return '<p> thx for using this  nitro gen and thx for 120 subs on my yt</p> <p><strong>slicybtw</p> </strong>'
print("hositng on 8080 port")
Thread(target=app.run,args=("0.0.0.0",8080)).start()