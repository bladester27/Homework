def printer(**printrows: str) -> None:
  for key in printrows:
    print(key, printrows[key])

printer(breakfast='eggs', lunch='spam', dinner='ham')
var = (breakfast='eggs', lunch='spam', dinner='ham')