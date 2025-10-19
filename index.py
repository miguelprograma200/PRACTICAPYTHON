from flask import Flask, render_template,request
app = Flask(__name__)

# rutas base 
@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/nosotros")
def nosotros():
    return render_template("nosotros.html")

@app.route("/eje1")
def eje1():
    return render_template("eje1.html")

@app.route("/eje2")
def eje2():
    return render_template("eje2.html")

@app.route("/eje3")
def eje3():
    return render_template("eje3.html")

@app.route("/eje4")
def eje4():
    return render_template("eje4.html")

@app.route("/eje5")
def eje5():
    return render_template("eje5.html")

@app.route("/eje6")
def eje6():
    return render_template("eje6.html")

@app.route("/eje7")
def eje7():
    return render_template("eje7.html")

@app.route("/eje8")
def eje8():
    return render_template("eje8.html")

@app.route("/eje9")
def eje9():
    return render_template("eje9.html")

@app.route("/eje10")
def eje10():
    return render_template("eje10.html")


#backend de cada una de las rutas junto logica
@app.route("/respuesta", methods=["POST"])
def respuesta():
    if request.method == "POST" :
        n1 = float(request.form["n1"])
        n2 = float(request.form["n2"])
        n3 = float(request.form["n3"])
        suma = n1 + n2 + n3
        return render_template("index.html", res=suma) # retorno 


@app.route("/ejercicio1", methods=["POST"])
def ejercicio1():
    if request.method == "POST" :
        nta1 = float(request.form["nta1"])
        nta2 = float(request.form["nta2"])
        nta3 = float(request.form["nta3"])
        promedio = (nta1 + nta2 + nta3) / 3
        return render_template("eje1.html", pro=promedio )
   

  
@app.route("/ejercicio2", methods=["POST"])
def ejercicio2():
    
    categoria_resultado = ""

    if request.method == "POST" :    
        
        edad = int(request.form["edad"])
       
        
        if 0 <= edad <= 12:
            categoria_resultado = "Niño"
       
        elif 13 <= edad <= 17:
            categoria_resultado = "Adolescente"
        
        elif 18 <= edad <= 64:
            categoria_resultado = "Adulto"
       
        elif edad >= 65:
            categoria_resultado = "Adulto mayor"
        
        else:
            categoria_resultado = "Edad no válida"
            
    return render_template("eje2.html", categoria=categoria_resultado)



@app.route("/ejercicio3", methods=["POST"])
def ejercicio3():

    lados_resultados =""

    if request.method == "POST" :
        
        lado1 = int(request.form["lado1"])
        lado2 = int(request.form["lado1"])
        lado3 = int(request.form["lado3"])

        if lado1 == lado2 == lado3:
            lados_resultados =  "Equilatero."

        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
             lados_resultados = "Isosceles."

        else:
           lados_resultados= "Escaleno."        

    return render_template("eje3.html",lados=lados_resultados)



@app.route("/ejercicio4", methods=["POST"])
def ejercicio4():
        
    numes = ""

    if request.method == "POST" :
               
      nunmes = int(request.form["nunmes"])

      if  nunmes == 1:
          numes = "Enero"
      elif nunmes == 2:
          numes = "Febrero"    
      elif nunmes == 3:
          numes = "Marzo" 
      elif nunmes == 4:
          numes = "Abril" 
      elif nunmes == 5:
          numes = "Mayo" 
      elif nunmes == 6:
          numes = "Junio" 
      elif nunmes == 7:
          numes = "Julio"
      elif nunmes == 8:
          numes = "Agosto"  
      elif nunmes == 9:
          numes = "Septiembre" 
      elif nunmes == 10:
          numes = "Octubre"
      elif nunmes == 11:
          numes = "Noviembre" 
      elif nunmes == 12:
          numes = "Diciembre" 
      else:
          numes = "Numero invalido.Ingrese un numero entre 1 y 2"           

    return render_template("eje4.html" , nunnm=numes)



@app.route("/ejercicio5", methods=["POST"])
def ejercicio5():

    numeros = ""

    if request.method  =="POST":

     num1 = int(request.form["num1"])
     num2 = int(request.form["num2"])
     operacion =request.form["operacion"]

     if operacion == "+":
         resultado = num1 + num2
         numeros = (f" Suma es: {resultado}")
          
     elif operacion =="-":
         resultado = num1 - num2
         numeros = (f"Resta es: {resultado}")

     elif operacion == "*":
         resultado =num1 * num2
         numeros = (f"Multiplicacion es: {resultado}")

     elif operacion ==  "/":
         if num2 != 0:
            resultado = num1 / num2
            numeros = (f"Division es: {resultado}")
         else:
             resultado = (f"Error: No se puede dividir entre cero.")

     else:
         resultado = "Operacion no valida. ingrese una operacion valida (+,-,*,/)."

    return render_template("eje5.html", numerosss=numeros)     



@app.route("/ejercicio6", methods=["POST"])
def ejercicio6():
    mensaje = ""
    if request.method == 'POST':
        antiguedad = int(request.form["antiguedad"])
        if antiguedad < 5:
            bono = 100
        elif 5 <= antiguedad <= 10:
            bono = 200
        else:
            bono = 300
        mensaje = f" ${bono}"
    return render_template("eje6.html", variabless=mensaje)

@app.route("/ejercicio7", methods=["POST"])
def ejercicio7():
    resultado = ""
    if request.method == 'POST':
        Num = int(request.form["Num"])
        if Num > 0:
            if Num % 2 == 0:
                resultado = "Es positivo y par."
            else:
                resultado = "Es positivo e impar."
        elif Num < 0:
            resultado = "  Es negativo."
        else:
            resultado = "Es cero."
    return render_template("eje7.html", par_impar=resultado)

@app.route("/ejercicio8", methods=["POST"])
def ejercicio8():
    mensaje = ""
    if request.method == 'POST':
        peso = float(request.form["peso"])
        altura = float(request.form["altura"])
        imc = peso / (altura ** 2)
        if imc < 18.5:
            categoria = "Bajo peso"
        elif 18.5 <= imc <= 24.9:
            categoria = "Peso normal"
        elif 25 <= imc <= 29.9:
            categoria = "Sobrepeso"
        else:
            categoria = "Obesidad"
        mensaje = f"Tu IMC es: {round(imc,2)}, Categoría: {categoria}"
    return render_template("eje8.html", peso_altura=mensaje)

@app.route("/ejercicio9", methods=["POST"])
def ejercicio9():
    digito = ""
    if request.method == 'POST':
        num = abs(int(request.form["num"]))  # Asegura positivo
        if num < 10:
            digito = "1 dígito."
        elif num < 100:
            digito = " 2 dígitos."
        elif num < 1000:
            digito = "3 dígitos."
        elif num < 10000:
            digito = " 4 dígitos."
        else:
            digito = " 4 dígitos."
    return render_template("eje9.html", digitos=digito)

@app.route("/ejercicio10", methods=["POST"])
def ejercicio10():
    mensaje = ""
    if request.method == 'POST':
        cantidad = int(request.form["cantidad"])
        precio_unitario = 80000
        subtotal = cantidad * precio_unitario
        if cantidad > 30:
            descuento = 0.4
        elif 21 <= cantidad <= 30:
            descuento = 0.2
        elif 11 <= cantidad <= 20:
            descuento = 0.1
        else:
            descuento = 0
        total = subtotal - (subtotal * descuento)
        mensaje = f"Total a pagar: ${total:.2f}"
    return render_template("eje10.html", cantidad_zapatos=mensaje)

if __name__ == '__main__':
    app.run(debug=True)
