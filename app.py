from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def tax_calculator():
    if request.method == 'POST':
        # Get form data
        month = request.form['month']
        year = request.form['year']
        gross_salary = float(request.form['gross-salary'])
        net_salary = float(request.form['net-salary'])
        
        # Calculate annual salary
        annual_salary = gross_salary * 12
        annual_tax = 0
        
        # Calculate tax based on the annual salary
        if annual_salary <= 600000:
            annual_tax = 0
        elif 600000 < annual_salary <= 1200000:
            annual_tax = (annual_salary - 600000) * 0.05
        elif 1200000 < annual_salary <= 2200000:
            annual_tax = 30000 +  (  (annual_salary - 1200000) * 0.15)

        elif 2200000 < annual_salary <= 3200000 :
            annual_tax = 165000 + ( (annual_salary - 2200000) * 0.225)    
       
        else:  # annual_salary > 6000000
            annual_tax = (1200000 - 600000) * 0.025 + (2400000 - 1200000) * 0.15 + (3000000 - 2400000) * 0.20 + (6000000 - 3000000) * 0.25 + (annual_salary - 6000000) * 0.30
        
        # Render the result in the template
        return render_template('index.html', 
                               annual_salary=annual_salary, 
                               annual_tax=annual_tax)
    
    return render_template('index.html', annual_salary=None, annual_tax=None)

if __name__ == '__main__':
    app.run(debug=True)

