from transformers import AutoTokenizer, AutoModelForCausalLM
from huggingface_hub import login
import requests
import torch
import socket
import threading

login("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")

tokenizer = AutoTokenizer.from_pretrained("Bhuvanesh-Ch/summarizationFineTuned")
model = AutoModelForCausalLM.from_pretrained("Bhuvanesh-Ch/summarizationFineTuned")



def handle_client(client_socket, parameter):
    # Function to be called when a client connects
    print(f"Received connection from {client_socket.getpeername()} with parameter: {parameter}")
    parameter = "Summarize the follwing case details " + parameter
    inputs = tokenizer(parameter, return_tensors='pt')
    response = tokenizer.decode(
                            model.generate(
                                inputs["input_ids"],
                                max_new_tokens=600,
                            )[0],
                         skip_special_tokens=True
                        )
    
    client_socket.send(response.encode())
    
    # Close the client socket
    client_socket.close()





def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 2000))
    server.listen(5)

    print("[*] Listening on 127.0.0.1:9005")

    while True:
        client, addr = server.accept()
        print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")
        
        # Receive parameter from the client
        parameter = client.recv(9000).decode()
        
        # Create a new thread to handle the client with the received parameter
        client_handler = threading.Thread(target=handle_client, args=(client, parameter))
        client_handler.start()

start_server()




                
