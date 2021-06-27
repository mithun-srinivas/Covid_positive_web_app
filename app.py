from flask import Flask,render_template,request
import gspread

gc = gspread.service_account(filename='credentials.json')
sh = gc.open_by_key('13ZVcLC0PuOOu7oDE2OdUD0LtogbYkjWH-Up_Z9n45QU')
worksheet = sh.sheet1

app = Flask(__name__)



@app.route('/')
def hello_world():
   return render_template('index.html')

@app.route('/form', methods=['POST','GET'])
def form():
   if request.method == 'POST':
      date = request.form['date']
      feedback = request.form['feedback']
      print(date)
      print(feedback)
      user = [date,feedback]
      i=2
      worksheet.insert_row(user,2)

    

   return render_template('form.html')



@app.route('/awareness')
def awareness():
    value1 =worksheet.get('B2')
    print(value1[0][0])
    value2 =worksheet.get('B3')
    print(value2[0][0])
    value3 =worksheet.get('B4')
    print(value3[0][0])
    value4 =worksheet.get('B1')
    print(value4[0][0])
    return render_template('awareness.html',value1=value1[0][0],value2=value2[0][0],value3=value3[0][0],value4=value4[0][0])
       
       
      
      
 
 

@app.route('/about')
def about():
   return render_template('about.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)