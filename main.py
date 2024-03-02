import hashlib
import datetime as date

# bloco único
class Block:
    def __init__(self, index, timestamp, data, previous_hash) -> None:
        self.index = index # o índice do bloco
        self.timestamp = timestamp # registra o tempo que o bloco foi criado
        self.data = data # o dado guardado no bloco
        self.previous_hash = previous_hash # hash do bloco anterior
        self.hash = self.calculate_hash() # a hash deste bloco

    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update(
            str(self.index).encode("utf-8") +
            str(self.timestamp).encode("utf-8") +
            str(self.data).encode("utf-8") +
            str(self.previous_hash).encode("utf-8")
        )
        return sha.hexdigest()
    
# cadeia de blocos ou blockchain

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
    
    def create_genesis_block(self):
        return Block(0, date.datetime.now(), "Genesis block", "0")

