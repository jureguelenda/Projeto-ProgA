def descendentes(arv):
     if arv[1] == []:
          return []
     else:
          return[desc for filho in arv[1] for desc in [filho[0]] + descendentes(filho)]

arv = ( "Maria", [ ("Joana", [ ("Lucio", []),
                               ("Jõao", [])
                             ]
                   ),
                   ("Pedro",[]),
                   ("Patricia", [ ("Marina", [ ("Marcelo", []),
                                               ("Tomás", [])
                                             ]
                                  )
                                ]
                   ),
                   ("Marcos",[])
                 ]
      )

print(descendentes(arv))