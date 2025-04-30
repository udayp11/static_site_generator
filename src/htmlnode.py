class HTMLNode:
    def __init__(self,tag = None,value = None,children = None,props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        string = ""
        for prop in self.props:
            string += f' {prop}="{self.props[prop]}"'
            return string

    def __repr__(self):
        return f"HTMLNode({self.tag},{self.value},{self.children},{self.props})"


class LeafNode(HTMLNode):
    def __init__(self,tag,value,props=None):
        super().__init__(tag,value,None,props)

    def to_html(self):
        
        if self.value == None:
            raise ValueError("Invalid HTML: no value")
        elif self.tag == None:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):

        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(self,tag,children,props=None):
        super().__init__(tag,None,children,props)
    def to_html(self):
        
        if self.tag is None:
            raise ValueError("Invalid HTML: no value")
        if self.children is None:
            raise ValueError("Invalid : no children")

        child_string = ""

        for child in self.children:
            child_string += child.to_html()

        return f"<{self.tag}{self.props_to_html()}>{child_string}</{self.tag}>"

    def __repr__(self):

        return f"ParentNode({self.tag},{self.children},{self.props})"
            
    

        

            
        


        


    

    

        
    
