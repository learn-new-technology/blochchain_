from BlockChain import BlockChain

a = BlockChain(5)

a.add_block({
    "name": "THI-EN-HI",
    "age": 18,
    "value": "1000$"
})

a.add_block({
    "name": "KIM",
    "age": 20,
    "value": "5000$"
})

a.add_block({
    "name": "HI",
    "age": 7,
    "value": "99999$"
})

print(a.is_valid())

