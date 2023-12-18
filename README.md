# Multiplayer AI Powered Game

## Description

This project includes a basic implementation of a multiplayer game server and a simple client using Python's socket programming. The server manages multiple client connections, maintains a game state, and broadcasts updates to all connected clients.

## Project Structure

All code files are inside the `src` folder.

- `server/`:
  - `server.py`: Configure and start server.
  - `client_thread.py`: Thread defined for handling each individual client.
- `client/`:
  - `client.py`: Configure and connect to server.
  - `game_thread.py`: Handles running pygame based on game state.
  - `receive_thread.py`: Thread for receiving server messages and updating the game state.
- `game/`:
  - `game_state.py`: Singleton class storing the state of the game on client and server to synchronize the information and render the game.

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/Konstantin-nik/python2module_ImageProgram.git
   cd python2module_ImageProgram
   ```

2. Install the required packages:

   - NOTE: Recommended to make a virtual environment.

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1.  Run an instance of the server:

    ```bash
    cd src/server
    python server.py
    ```

2.  Run as many instances of client as you want:
    ```bash
    cd src/client
    python client.py
    ```

- Ensure the server's IP address and port in the client code match those in the server code.