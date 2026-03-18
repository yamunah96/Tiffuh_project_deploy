from flask import Flask,render_template,request
from calcultor import YieldCalculator

app= Flask(__name__)
crop_type=["wheat","corn","rice","soybean","barley"]

@app.route("/",methods=["GET","POST"])
def index():
    result= None
    summary=None
    error= None
    if request.method =="POST":
        try:
            area= float(request.form["area"])
            area_unit= request.form["unit"]
            crops= request.form["crop"]
            _yield_unit= float(request.form["yield"])

            # validation checks
            if area <=0:
                raise ValueError("Area must be greater than 0")
            if area_unit not in ["acres","hectares"]:
                raise ValueError("Invalid unit selected")
            if crops not in crop_type:
                raise ValueError("Inavalid crop type selected")
            if _yield_unit <=0:
                raise ValueError("Yield per unit must be greater than 0")
            
            total_validation= YieldCalculator.calculate_total_yeild(area,_yield_unit)
            result= total_validation
            summary={
                "area":area,
                "unit":area_unit,
                "crop":crops,
                "yield_per_unit":_yield_unit
            }
        except ValueError as e:
            error= str(e)
        except Exception:
            error= "unexcpected error occured, Try again"
    return render_template("index.html",crops=crop_type,result=result,summary=summary,error=error)

if __name__ == "__main__":
    app.run(debug=True)

