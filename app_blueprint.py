from flask import  Blueprint, render_template, request

app_blueprint = Blueprint('app', __name__)

@app_blueprint.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        global position, decimal, decimalf
        data: str
        data = request.form.get('bin', '0')
        print(data)
        for a in data:
            if a == '0' or a == '1' or '':
                pass
            else:
                return render_template('index.html', value='Error! Please insert a binary code.')
        position = int(len(data)) - 1
        decimal = 0
        decimalf = 0
        print(position)
        for b in data:
            b2 = int(b)
            print('ab', b, b2, position, decimal, decimalf)

            base2 = 2 ** position
            decimal = base2 * b2
            decimalf = decimal + decimalf

            position = position - 1

            print(b, b2, base2, position, decimal, decimalf)


        return render_template('index.html', value=int(decimalf))

    else:
        return render_template('index.html')

