from flask import Flask , request , Response 

data = None

app = Flask(__name__)

@app.route('/send_frame'  , methods = ['POST'])
def receive_frame():
    print(request.method)
    if request.method == 'POST':
        global data
        data = request.data

        return Response(status=200)
    
    else:
        return Response(status=400)

def generate_frames():
    while True:
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + data + b'\r\n')

# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/video')
def video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(host ='0.0.0.0' , debug = False)