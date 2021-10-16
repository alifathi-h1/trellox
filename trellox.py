from trello import TrelloClient
import pprint, requests,os              

client = TrelloClient(
    api_key=os.environ.get('Trello_API_KEY'),
    token=os.environ.get('Trello_API_TOKEN'),)
    
attachments = []

def list_all_boards(client):
    """
        get list of all boards to determine the ID
        for further functions
    """
    all_boards = client.list_boards()
    for counter, board in enumerate(all_boards):
        print(counter, board.name)


# list_all_boards(client)
def print_cards_from_board(board_id, client):
    """
        Access board with ID board_id in the client instance
        and print all non-archived lists with their non-archived cards 
    """
    all_boards = client.list_boards()
    
    my_board = all_boards[board_id] 
    all_lists_on_board = my_board.list_lists()
    
    for list in all_lists_on_board:
        for card in list.list_cards():
        
            print(str(card.board.name + ":" + card.description) + ":" +str(card.name))
               

for x in range(1, 30): 
    print_cards_from_board(x, client)

