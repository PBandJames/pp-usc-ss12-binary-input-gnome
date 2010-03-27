#!/usr/bin/env python
# This Python file uses the following encoding: utf-8


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
    def __str__(self):
        return self.value

class MorseTree:
    def __init__(self, alpha_root, num_punct_node):
        self.alpha_root = alpha_root
        self.current_node = alpha_root
        self.num_punct_root = num_punct_node
        self.current_tree = "alpha"

    def reset(self):
        if self.current_tree == "alpha":
            self.current_node = self.alpha_root
        if self.current_tree == "num_punct":
            self.current_node = self.num_punct_root

    def dot(self):
        self.current_node = self.current_node.left
        return self.current_node

    def dash(self):
        self.current_node = self.current_node.right
        return self.current_node

    def leaf(self):
        if not self.current_node.left and not self.current_node.right:
            return True
        else:
            return False

    def get_current_node(self):
        return self.current_node

    def switch_trees(self):
        if self.current_tree == "alpha":
            self.current_tree = "num_punct"
            self.current_node = self.num_punct_root
        elif self.current_tree == "num_punct":
            self.current_tree = "alpha"
            self.current_node = self.alpha_root

    def __str__(self):
        return self.current_node.value

def get_morse_tree():
    root = TreeNode(65408)

    # normal alphabet
    node_a = TreeNode("a")
    node_b = TreeNode("b")
    node_c = TreeNode("c")
    node_d = TreeNode("d")
    node_e = TreeNode("e")
    node_f = TreeNode("f")
    node_g = TreeNode("g")
    node_h = TreeNode("h")
    node_i = TreeNode("i")
    node_j = TreeNode("j")
    node_k = TreeNode("k")
    node_l = TreeNode("l")
    node_m = TreeNode("m")
    node_n = TreeNode("n")
    node_o = TreeNode("o")
    node_p = TreeNode("p")
    node_q = TreeNode("q")
    node_r = TreeNode("r")
    node_s = TreeNode("s")
    node_t = TreeNode("t")
    node_u = TreeNode("u")
    node_v = TreeNode("v")
    node_w = TreeNode("w")
    node_x = TreeNode("x")
    node_y = TreeNode("y")
    node_z = TreeNode("z")

    # numbers
    node_0 = TreeNode("0")
    node_1 = TreeNode("1")
    node_2 = TreeNode("2")
    node_3 = TreeNode("3")
    node_4 = TreeNode("4")
    node_5 = TreeNode("5")
    node_6 = TreeNode("6")
    node_7 = TreeNode("7")
    node_8 = TreeNode("8")
    node_9 = TreeNode("9")

    # punctuation
    node_plus = TreeNode("+")
    node_dash = TreeNode("-")
    node_apostrophe = TreeNode("'")
    node_quote = TreeNode("\"")
    node_exclamation = TreeNode("!")
    node_question = TreeNode("?")
    node_semicolon = TreeNode(";")
    node_colon = TreeNode(":")
    node_comma = TreeNode(",")
    node_period = TreeNode(".")
    node_underscore = TreeNode("_")
    node_equals = TreeNode("=")
    node_slash = TreeNode("/")
    node_backslash = TreeNode("\\")
    node_at = TreeNode("@")
    node_dollar = TreeNode("$")
    node_open_parentheses = TreeNode("(")
    node_close_parentheses = TreeNode(")")
    node_up = TreeNode("up")
    node_down = TreeNode("down")
    node_left = TreeNode("left")
    node_right = TreeNode("right")

    # control keys (pref/num and punctuation)
    node_pf = TreeNode("pf");
    node_num_punct = TreeNode("num_punct")
    node_abc = TreeNode("abc")

    # first level
    root.left = node_e
    root.right = node_t

    # second level
    node_e.left = node_i
    node_e.right = node_a

    node_t.left = node_n
    node_t.right = node_m

    # third level
    node_i.left = node_s
    node_i.right = node_u

    node_a.left = node_r
    node_a.right = node_w

    node_n.left = node_d
    node_n.right = node_k

    node_m.left = node_g
    node_m.right = node_o

    # fourth level
    node_s.left = node_h
    node_s.right = node_v

    node_u.left = node_f

    node_r.left = node_l

    node_w.left = node_p
    node_w.right = node_j

    node_d.left = node_b
    node_d.right = node_x

    node_k.left = node_c
    node_k.right = node_y

    node_g.left = node_z
    node_g.right = node_q

    node_o.left = node_pf
    node_o.right = node_num_punct

    # second tree
    node_abc.left = node_period
    node_abc.right = node_comma

    # 
    node_period.left = node_question
    node_period.right = node_exclamation

    node_comma.left = node_at
    node_comma.right = node_0

    #
    node_question.left = node_1
    node_question.right = node_2

    node_exclamation.left = node_3
    node_exclamation.right = node_4

    node_at.left = node_5
    node_at.right = node_6

    node_0.left = node_7
    node_0.right = node_8

    # 
    node_1.left = node_9
    node_1.right = node_underscore

    node_2.left = node_quote
    node_2.right = node_apostrophe

    node_3.left = node_dash
    node_3.right = node_slash

    node_4.left = node_open_parentheses
    node_4.right = node_close_parentheses

    node_5.left = node_backslash
    node_5.right = node_colon

    node_6.left = node_semicolon
    node_6.right = node_dollar

    node_7.left = node_plus
    node_7.right = node_equals

    node_8.left = node_up
    node_8.right = node_down

    # ninth level
    node_down.left = node_left;
    node_down.right = node_right;

    return MorseTree(root, node_abc)

