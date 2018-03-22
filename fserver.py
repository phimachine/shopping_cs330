from flask import Flask, Response, request, send_from_directory
from flask_cors import CORS
import random, json

app=Flask(__name__, static_url_path='')
CORS(app)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)

@app.route('/')
def _3():
    return """
    <html>
    <head>
        <!-- https://www.w3schools.com/bootstrap/bootstrap_get_started.asp -->
        <title>Shopping List Application</title>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
        <link rel="stylesheet" href="css/shoppingstyle.css">        
    </head>

    <body> 
        <div class="container">
                <nav class="navbar navbar-default">
                        <div class="container-fluid">
                          <div class="navbar-header">
                            <a class="navbar-brand" href="#">Shopping List</a>
                          </div>
                          <ul class="nav navbar-nav">
                            <li class="active"><a href="#">Home</a></li>
                            <li><a href="#">Page 1</a></li>
                            <li><a href="#">Page 2</a></li>
                            <li><a href="#">Page 3</a></li>
                          </ul>
                        </div>
                      </nav>
            <div class="panel panel-default col-md-12">
                <div class="panel-body">
                <div class="row form-inline">

                <div class="form-group">
                    <label for="itemname">Item Name</label>
                    <input type=text class="form-control" name="itemname" id=itemname />
                </div>
                <div class="form-group">
                <label for="qty">Quantity</label>
                <select name="quantity" id="qty" class="form-control">
                    <option value="1">1</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                    <option value="4">4</option>
                    <option value="5">5</option>
                    <option value="6">6</option>
                    <option value="7">7</option>
                    <option value="8">8</option>
                    <option value="9">9</option>
                    <option value="10">10</option>                                                                                                                                                                                                                                                   
                </select>
                </div>
                <div class="form-group">
                <label for="priority">Priority</label>
                <select name="priority" id="priority" class="form-control">
                    <option value="low">low</option>
                    <option value="medium">medium</option>
                    <option value="high">high</option>
                </select>
            </div>
                </div>

                <div class="row form-inline" style="margin-top: 20px; margin-bottom: 20px;">
                    <div class="form-group">
                    <label for="store">Store Name</label>
                    <select name="store" id="store" class="form-control">
                    </select>
                    </div>
                    <div class="form-group">
                    <label for="category">Store Section</label>
                    <select name="category" id="category" class="form-control">
                    </select>
                    </div>
                    <div class="form-group">
                    <label for="price">Price</label>
                    <input type="text" name="price" id="price" class="form-control">
                    </div>
                </div>
                <div class="form-inline" style="float: right;">
                    <button onclick="removeAll()" class ="btn btn-primary" id=removebutt>Remove All</button>
                    <button onclick="loadShoppingList()" class ="btn btn-primary" id=loadbutt>Load List</button>
                    <button onclick="saveShoppingList()" class ="btn btn-primary" id=savebutt>Save List</button>
                    <button onclick="clickedAddItem()" class="btn btn-primary" id=gobutt>Add Item</button>
                </div>
                </div>
            </div>
            <div class="col-md-12">
            <table class="table table-bordered">
                <thead>
                    <tr>
                        <th></th><th>Item</th><th>Quantity</th><th>Store</th><th>Section</th><th>Price</th>
                    </tr>
                </thead>
                <tbody id="shoppinglist"></tbody>
            </table>
            </div>
        </div>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
        <script src="js/storage.js?x=2" type=text/javascript></script>
        <script src="js/model.js?x=2" type=text/javascript></script>
        <script src="js/view.js?x=2" type=text/javascript></script>        
        <script src="js/flaskio.js?x=2" type=text/javascript></script>
        <script src="js/shopping.js?x=2" type=text/javascript></script>
    </body>
</html>

    """


@app.route('/getshoppinglist')
def _():
    with open("shoppingList.json", "r") as datafile:
        raw=json.load(datafile)
        res=Response(raw)
        res.headers['Content-type'] = 'application/json'
        return res

@app.route('/saveshoppinglist',methods=['POST'])
def _2():
    raw=request.data
    with open("shoppingList.json", "w") as datafile:
        json.dump(raw, datafile)


if __name__=="__main__":
    app.run(debug=True, port=5001)
