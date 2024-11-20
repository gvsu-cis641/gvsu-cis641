from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
  return 'Server Works!'

@app.route('/cis641')
def cis641():
  return "<img src='https://i.makeagif.com/media/5-21-2015/5kUbPs.gif' />Class is over hoorayyyyy!"

@app.route('/cis437/hello/<user_id>')
def cis437(user_id):
  print(user_id)
  return f"The user is {user_id}"


@app.route('/cis350')
def hello_there():
#  return 'Hey there 350 hope you have a gr8 weekend ... m8'

  templateData = {
            'message': "https://media.tenor.com/5ety3Lx3QccAAAAC/its-fine-dog-fine.gif",
    }
  return render_template('cis350.html', **templateData)
  
@app.route('/greet')
def say_hello():
  return 'Hello from Server'

@app.route('/msg')
def say_msg():
    import random
    msgs = ['hello there', 'hey', 'hello world', 'hello universe']
    random.shuffle(msgs)
    templateData = {
      'message': msgs[0]
    }
    return render_template('msg.html', **templateData)
            

if __name__ == "__main__":
  app.run()
