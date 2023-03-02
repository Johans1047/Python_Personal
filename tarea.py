from collections import OrderedDict

clients = {
    "name": ["Abel Murgas", "Jose Martinez", "Roberto Rodriguez", "Carlos Sanjur"],
    "age": [25, 23, 42, 34],
    "grade": [91, 90, 88, 45],
    "group": ["A1", "A2", "B3", "B3"]
}

def get_complete_information(clients:dict) -> list:
  """
    This method is for transforming and concatenating the values corresponding to a single customer into a single list.
    Args:
        clients (dict): dict variable
    Returns:
        list:  complete_list
  """

  complete_list = []
  
  for i in range(len(clients)):
    list = []
    for key in clients:    
      list.append(clients[key][i])
    complete_list.append(list)
  
  return complete_list

  """
    Output:
    [[name, age, grade, group]^n]
  """
  pass

def order_by_grade_asc(clients:list) -> list:
  """
    This method is for sorting the lists in ascending order according to the grade.
    Args:
        clients (list): list variable
    Returns:
        list: clients
  """
  
  list = []
  for i in range(len(clients)):
    list.append(clients[i][2])  
  
  for i in range(len(list)):
    
    minimum_index = i
    for j in range(i+1, len(list)):
      if list[j] < list[minimum_index]:
        minimum_index = j
        list[i], list[minimum_index] = list[minimum_index], list[i]
        
  j = 3
  
  while j >= 0:
    for i in range(len(clients)):
      if clients[i][2] == list[j]:
        aux = clients.pop(i)           
        index = list.index(list[j])        
        clients.insert(index, aux)
        
    j = j - 1
    
  return clients 

def order_by_grade_desc(clients:list) -> list:
  """
    This method is for sorting the lists in descending order according to the grade.
    Args:
        clients (list): list variable
    Returns:
        list: clients
  """
  
  list = []
  for i in range(len(clients)):
    list.append(clients[i][2])  
  
  for i in range(len(list)):
    
    maximum_index = i
    for j in range(i+1, len(list)):
      if list[j] > list[maximum_index]:
        maximum_index = j
        list[i], list[maximum_index] = list[maximum_index], list[i]
        
  j = 3
  
  while j >= 0:
    for i in range(len(clients)):
      if clients[i][2] == list[j]:
        aux = clients.pop(i)           
        index = list.index(list[j])        
        clients.insert(index, aux)
        
    j = j - 1
    
  return clients
  
def group_by_group(clients:list) -> dict:
  """
    This method is for sorting within a dictionary all the customers belonging to a corresponding group.
    Args:
        clients (list): list variable
    Returns:
        dict: Output
  """
  
  Output = {}
  
  list_org = []
  for i in range(len(clients)):
    list_org.append(clients[i][3]) 
  
  list_ordered = list(OrderedDict.fromkeys(list_org))
  
  for i in range(len(list_ordered)):
    Output[list_ordered[i]] = ""
  
  for i in range(len(list_ordered)):  
    
    if clients[i][3] == list_ordered[i]:      
      array = []
      array.append(clients[i][0])
      Output[list_ordered[i]] = array
      
      if i == 2:
        array.pop()
        array.append(clients[i][0])
        array.append(clients[i+1][0])
        Output[list_ordered[i]] = array  
        
  return Output
  
  """
    Output:
    {
    "A1": ["Abel Mugas"],
    "A2": ["Jose Martine"],
    "B3": ["Roberto Rodrigue", "Carlos Sanjur"]
    }
  """
  pass

if __name__ == "__main__":
  
  complete_information = get_complete_information(clients)
  print(order_by_grade_asc(complete_information))
  print(order_by_grade_desc(complete_information))
  print(group_by_group(complete_information))