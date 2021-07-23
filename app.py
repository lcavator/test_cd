from flask import Flask, render_template
import random

app = Flask(__name__)

# list of images to show
images = [
"https://www.animatedimages.org/data/media/50/animated-flower-image-0050.gif",
"https://www.animatedimages.org/data/media/50/animated-flower-image-0051.gif",
"https://www.animatedimages.org/data/media/50/animated-flower-image-0052.gif",
"https://www.animatedimages.org/data/media/50/animated-flower-image-0053.gif",
"https://www.animatedimages.org/data/media/50/animated-flower-image-0054.gif",
"https://www.animatedimages.org/data/media/50/animated-flower-image-0055.gif",
"https://www.animatedimages.org/data/media/50/animated-flower-image-0056.gif"
]

@app.route('/')

def index():
   url = random.choice(images)
   return render_template('index.html',url=url)

if __name__ == "__main__":
         app.run(host="0.0.0.0")

