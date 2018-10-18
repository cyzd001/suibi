# import git
#
# git.Repo.repo.clone('clone_path')

from xml.dom import minidom
from xml.dom.minidom import parse
from xml.etree import ElementTree
from xml.etree.ElementTree import ElementTree,Element
import xml.etree.ElementTree as ET
doc = ET.parse(u"D:/测试环境/aus-nk-bank/WEB-INF/classes/spring.xml")
# print(doc.getroot().tag)
root = doc.getroot()
# print(root.tag)
list=[]
for i in root:
    # print(i.tag)
    # print(i.attrib)
    for j in i:
        print(j.attrib)
        num = j.attrib
        list.append(num)

    # for j in i:
    #     # if i.attrib['id']=="extbankDatasourceDg":
    #         print(j.tag)
    #         print(j.attrib)

stm = parse(u"D:/测试环境/aus-nk-bank/WEB-INF/classes/spring.xml")
strm=[]
for node in stm.getElementsByTagName("bean"):
    # 获取标签ID属性
    value_str = node.getAttribute("id")
    strm.append(value_str)
    print(strm)  # 打印输出
    # if value_str =="extbankDatasourceDg":
    #     print(doc.getroot().iter("property"))
# import xml.dom.minidom
# from xml.dom import Node
#
# list=[]
# dom = xml.dom.minidom.parse(u"D:/测试环境/aus-nk-bank/WEB-INF/classes/spring.xml")
# root = dom.documentElement
# print(root.tag)
# for child in root.childNodes:
#  if child.nodeType == Node.ELEMENT_NODE:  # 是否是元素节点
#      dictAttr = {}
#      for key in child.attributes.keys():    # child.attrbutes.keys()查看所有属性，返回一个列表
#          attr = child.attributes[key]  # 返回属性地址
#          print(attr)
#          dictAttr[attr.name] = attr.value  # attr.name为属性名  attr.value为属性值
#          # print(attr.value)
#          list.append({child.nodeName: dictAttr})

# print(list)
# print(list[20])






def read_xml(in_path):
    '''读取并解析xml文件
      in_path: xml路径
      return: ElementTree'''
    tree = ElementTree()
    tree.parse(in_path)
    return tree
def write_xml(tree, out_path):
    '''将xml文件写出
      tree: xml树
      out_path: 写出路径'''
    tree.write(out_path, encoding="utf-8", xml_declaration=True)
def if_match(node, kv_map):
    '''判断某个节点是否包含所有传入参数属性
      node: 节点
      kv_map: 属性及属性值组成的map'''
    for key in kv_map:
        if node.get(key) != kv_map.get(key):
            return False
    return True
# ---------------search -----
def find_nodes(tree, path):
    '''查找某个路径匹配的所有节点
      tree: xml树
      path: 节点路径'''
    return tree.findall(path)
def get_node_by_keyvalue(nodelist, kv_map):
    '''根据属性及属性值定位符合的节点，返回节点
      nodelist: 节点列表
      kv_map: 匹配属性及属性值map'''
    result_nodes = []
    for node in nodelist:
        if if_match(node, kv_map):
            result_nodes.append(node)
    return result_nodes
# ---------------change -----
def change_node_properties(nodelist, kv_map, is_delete=False):
    '''修改/增加 /删除 节点的属性及属性值
      nodelist: 节点列表
      kv_map:属性及属性值map'''
    for node in nodelist:
        for key in kv_map:
            if is_delete:
                if key in node.attrib:
                    del node.attrib[key]
            else:
                node.set(key, kv_map.get(key))
def change_node_text(nodelist, text, is_add=False, is_delete=False):
    '''改变/增加/删除一个节点的文本
      nodelist:节点列表
      text : 更新后的文本'''
    for node in nodelist:
        if is_add:
            node.text += text
        elif is_delete:
            node.text = ""
        else:
            node.text = text
def create_node(tag, property_map, content):
    '''新造一个节点
      tag:节点标签
      property_map:属性及属性值map
      content: 节点闭合标签里的文本内容
      return 新节点'''
    element = Element(tag, property_map)
    element.text = content
    return element
def add_child_node(nodelist, element):
    '''给一个节点添加子节点
      nodelist: 节点列表
      element: 子节点'''
    for node in nodelist:
        node.append(element)
def del_node_by_tagkeyvalue(nodelist, tag, kv_map):
    '''同过属性及属性值定位一个节点，并删除之
      nodelist: 父节点列表
      tag:子节点标签
      kv_map: 属性及属性值列表'''
    for parent_node in nodelist:
        children = parent_node.getchildren()
        for child in children:
            if child.tag == tag and if_match(child, kv_map):
                parent_node.remove(child)
#2. 属性修改

tree = read_xml(u"D:/测试环境/aus-nk-bank/WEB-INF/classes/spring.xml")
#A. 找到父节点
nodes = find_nodes(tree, "bean/bean")
#B. 通过属性准确定位子节点
result_nodes = get_node_by_keyvalue(nodes, {"name":"url"})
#C. 修改节点属性
change_node_properties(result_nodes, {"value": "jdbc:oracle:thin:@192.168.55.5:1521:ljcprd "})
#主：jdbc:oracle:thin:@192.168.55.5:1521:ljcprd      备：jdbc:oracle:thin:@192.168.56.18:1521:ljcprdtest
   #D. 删除节点属性
# change_node_properties(result_nodes, {"value":""}, True)


# tree = ET.parse(u"D:/测试环境/aus-nk-bank/WEB-INF/classes/spring.xml")
# root = tree.getroot()  # f.seek(0)
# print(root)
# for node in root.iter('name'):
#     print(node)
    # new_year = int(node.text) + 1
    # node.text = str(new_year)
    # node.set('updated', 'yes')
# tree.write("xmltest.xml")


