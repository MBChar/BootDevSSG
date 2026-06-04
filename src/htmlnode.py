class HTMLNode:
    def __init__(self, tag: str = None, value: str = None, children = None, props:dict[str, str] = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __eq__(self, other):
        if self.tag != other.tag:
            return False
        if self.value != other.value:
            return False
        if self.props != other.props:
            return False
        if self.children is None and other.children is not None:
            return False
        if self.children is not None and other.children is None:
            return False
        if self.children is not None and other.children is not None:
            if len(self.children) != len(other.children):
                return False
            for child1, child2 in zip(self.children, other.children):
                if child1 != child2:
                    return False
        return True

    def to_html(self) -> str:
        raise NotImplementedError("to_html method not implemented for HTMLNode")
    
    def props_to_html(self) -> str:
        if self.props is None:
            return ""
        props_str = ""
        for key, value in self.props.items():
            props_str += f"{key}=\"{value}\" "
        return props_str
    
class LeafNode(HTMLNode):
    def __init__(
        self, tag: str | None, value: str, props: dict[str, str] | None = None
    ) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("invalid HTML: no value")
        if self.tag is None:
            return self.value
        props = self.props_to_html()
        if props:
            return f"<{self.tag} {props}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"

    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
class ParentNode(HTMLNode):
    def __init__(
        self, tag: str, children: list[HTMLNode], props: dict[str, str] | None = None
    ) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError("invalid HTML: no tag")
        if self.children is None:
            raise ValueError("invalid HTML: no children")
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        props = self.props_to_html()
        if props:
            return f"<{self.tag} {props}>{children_html}</{self.tag}>"
        else:
            return f"<{self.tag}>{children_html}</{self.tag}>"

    def __repr__(self) -> str:
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"