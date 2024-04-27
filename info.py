from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <html>
    <head>
        <title>2023 to 2024 12th Students Details</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {
                background-image: url('bg.png');
                background-size: cover;
                background-repeat: no-repeat;
                background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            .container {
                width: 320px;
                padding: 40px;
                background-color: rgba(255, 255, 255, 0.9);
                border-radius: 20px;
                box-shadow: 0 15px 35px rgba(0, 0, 0, 0.5);
                animation: fadeIn 0.5s ease;
            }
            h1 {
                text-align: center;
                color: #ffffff;
                margin-bottom: 40px;
                font-size: 28px;
                text-transform: uppercase;
                letter-spacing: 2px;
            }
            input[type="text"] {
                width: 100%;
                padding: 15px;
                margin-bottom: 20px;
                border: none;
                background-color: rgba(255, 255, 255, 0.8);
                border-radius: 5px;
                box-sizing: border-box;
                font-size: 16px;
                transition: background-color 0.3s ease;
                box-shadow: 0 3px 6px rgba(0, 0, 0, 0.1);
            }
            input[type="text"]:focus {
                background-color: rgba(255, 255, 255, 0.9);
            }
            input[type="text"]::placeholder {
                color: #999999;
            }
            button {
                width: 100%;
                padding: 15px;
                border: none;
                background-color: #fcb045;
                color: #ffffff;
                font-size: 18px;
                font-weight: bold;
                text-transform: uppercase;
                border-radius: 5px;
                cursor: pointer;
                transition: background-color 0.3s ease;
                box-shadow: 0 3px 6px rgba(0, 0, 0, 0.1);
            }
            button:hover {
                background-color: #f7951e;
            }
            @keyframes fadeIn {
                from {
                    opacity: 0;
                    transform: translateY(-20px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>2023 to 2024 12th Students Details</h1>
            <form action="/submit" method="post">
                <input type="text" name="name" placeholder="Name" required><br>
                <input type="text" name="reg_no" placeholder="Register No" pattern="[0-9]{7}" title="Please enter a 7-digit number" required><br>
                <input type="text" name="dob" placeholder="Date of Birth" required><br>
                <input type="text" name="cut_off" placeholder="Cut off" required><br>
                <button type="submit">Submit</button>
            </form>
        </div>
    </body>
    </html>
    '''

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    reg_no = request.form['reg_no']
    dob = request.form['dob']
    cut_off = request.form['cut_off']
    
    ip_address = request.remote_addr
    
    with open('info.txt', 'a') as file:
        file.write(f'{name}, {reg_no}, {dob}, {cut_off}, {ip_address}\n')
    
    return '''
    <html>
    <head>
        <title>Submission Successful</title>
        <style>
            body {
                background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            .container {
                width: 320px;
                padding: 40px;
                background-color: rgba(255, 255, 255, 0.9);
                border-radius: 20px;
                box-shadow: 0 15px 35px rgba(0, 0, 0, 0.5);
            }
            '''
if __name__ == '__main__':
    app.run(host='localhost', port=9876)
