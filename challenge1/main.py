from flask import Blueprint, jsonify, request
import json
import os

transaction_blueprint = Blueprint('transactions', __name__)

# Helper function to load transactions data from JSON file
def load_transactions():
    with open('transactions.json') as data_file:
        transactions_data = json.load(data_file)
    return transactions_data

@transaction_blueprint.route('/transaction/<id>', methods=['GET'])
def get_transaction(id):
    transactions_data = load_transactions()
    transaction = transactions_data.get(id, None)
    if transaction:
        return jsonify(transaction), 200
    else:
        return jsonify({"error": "Transaction not found"}), 404

@transaction_blueprint.route('/transaction', methods=['POST'])
def add_transaction():
    transactions_data = load_transactions()
    new_transaction = request.get_json()
    # Generate a new ID for the transaction
    new_id = str(len(transactions_data) + 1)
    transactions_data[new_id] = new_transaction

    with open('transactions.json', 'w') as data_file:
        json.dump(transactions_data, data_file, indent=4)
    
    print(f"Added transaction with ID: {new_id}")
    return jsonify({"message": "Transaction added successfully"}), 201

@transaction_blueprint.route('/transaction/<id>', methods=['PUT'])
def update_transaction(id):
    transactions_data = load_transactions()
    updated_transaction = request.get_json()
    if id in transactions_data:
        transactions_data[id] = updated_transaction

        with open('transactions.json', 'w') as data_file:
            json.dump(transactions_data, data_file, indent=4)
        
        print(f"Updated transaction with ID: {id}")
        return jsonify({"message": "Transaction updated successfully"}), 200
    else:
        return jsonify({"error": "Transaction not found"}), 404

@transaction_blueprint.route('/transaction/<id>', methods=['DELETE'])
def delete_transaction(id):
    transactions_data = load_transactions()
    if id in transactions_data:
        del transactions_data[id]
    
        with open('transactions.json', 'w') as data_file:
            json.dump(transactions_data, data_file, indent=4)
        
        print(f"Deleted transaction with ID: {id}")
        return jsonify({"message": "Transaction deleted successfully"}), 200
    else:
        return jsonify({"error": "Transaction not found"}), 404

@transaction_blueprint.route('/transactions', methods=['GET'])
def get_all_transactions():
    transactions_data = load_transactions()
    return jsonify(transactions_data), 200

# Run the Flask app
if __name__ == "__main__":
    from flask import Flask
    app = Flask(__name__)
    app.register_blueprint(transaction_blueprint, url_prefix="/api")
    app.run(debug=True)
