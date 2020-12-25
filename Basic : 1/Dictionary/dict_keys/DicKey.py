#Dictionary Keywords

dictionary = {
  'a' : [1,2,3], 
  'b' : 'hello',
  'x' : True,
  100 : [23,45],
  100 : [33,45],#same two key works bt show the upgraded value
  #[100] :34 ,#con't use because of Dict id imm
  '[100]':67
}

print (dictionary[100])
