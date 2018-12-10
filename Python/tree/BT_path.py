#python3
# find a node in a binary tree and print the path 

# call a DFS recursive routine
def findNode(node,v):
    stk = [];
    found = _recFind(node,v,stk);
    if found is None:
        print('Not Found')
    else:
        stk.append('root->{}'.format(node['value']))        
        print('Found',stk[::-1]);  
    
# backtrace after fionding a node        
def _recFind(node,v,stk):
    if node['value'] == v:        
        return 1;
    else:
        if node['left'] is not None:
            l = _recFind(node['left'],v,stk)
            if l is not None:
                stk.append('left->{}'.format(node['left']['value']));
                return 1;
        if node['right'] is not None:
            r = _recFind(node['right'],v,stk)
            if r is not None:
                stk.append('right->{}'.format(node['right']['value']));
                return 1;
    return None;

def main():
    tree = {
        'value' : 5,
        'left' : {
            'value' : 8,
            'left' : {
                'value' : 10,
                'left' : None,
                'right' : {
                    'value' : 12,
                    'left' : None,
                    'right' : None 
                }     
            },
            'right' : {
                'value' : 1,
                'left' : {
                    'value' : 25,
                    'left' : None,
                    'right' : None 
                },
                'right' : {
                    'value' : 85,
                    'left' : None,
                    'right' : {
                        'value' : 67,
                        'left' : None,
                        'right' : None     
                    } 
                }     
            }   
         },
        'right' : {
            'value' : 90,
            'left' : {
                'value' : 7,
                'left' : None,
                'right' : {
                    'value' : 14,
                    'left' : None,
                    'right' : None     
                }     
            },
            'right' : {
                'value' : 578,
                'left' : None,
                'right' : None     
            }
        }        
    }
    print(tree);
    print('----------');
    findNode(tree,67);
    
main();