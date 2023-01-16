from typing import NamedTuple
import re


class Token(NamedTuple):
    type: str
    value: str
    line: int
    column: int


def tokenize(code):
    # TODO: should add the rest of keywords in c++ in here.
	keywords = {'IF', 'THEN', 'ENDIF', 'FOR', 'NEXT', 'GOSUB', 'RETURN','auto','break','case','char','const','continue','default','do','double','else','enum','extern','float','for','goto','if','int','long','register','return','short','signed','sizeof','static','struct','switch','typedef','union','unsigned','void','volatile','while','asm','dynamic_cast','namespace','reinterpret_cast','bool','explicit','new','static_cast','false','catch','operator','template','friend','private','class','this','inline','public','throw','const_cast','delete','mutable','protected','true','try','typeid','typename','using','virtual','wchar_t','cout','cin','include'}
	token_specification = [
    # TODO: change this identifier redex it will only identify a string with letters no numbers or underscore.
	
	('NUMBER',                r'\d+(\.\d*)?'), # Numbers
	
	('Identifier', 			  r'(\w+)'),       # Identifiers
	
	('Line_comment' ,         r'(\/\/.+)'),    # Line comment
	
	('Multiline_comment' ,    r'(/\*([\s\S]*?)\*/\s*)'),    # Multi-Line comment
	
	('Single_qoute_char',     r'(\'.\')'),     # Single qoute character string
	
	('Single_qoute_string',   r'(\'.+\')'),    # Single qoute multi character string 
	
	('Double_qoute_string',   r'(\".+\")'),    # Single qoute multi character string 
	
	('Logical_operator',      r'\|{2}|&{2}|!'), #Logical Operators
	
	('Unary_operator',        r'\+{2}|-{2}'),	#Unary operators
	
	('Assignment_operator',   r'=\|\/=|\*=|%=|\+=|-='), #Assignment Operatprs
	
	('Arithmatic_operator',   r'\+|-|\/|\*|%'),	        # Arithmatic Operators
	
	('Bitwise_operator',	  r'&|\||\^|~|<<|>>'),      #Bitwise Operators
	
	('relational_operator',   r'>=|<=|<|>|==|!='),      #Relational Operators
	
	]
	
		
	tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
	line_num = 1
	line_start = 0
	for mo in re.finditer(tok_regex, code):
		kind = mo.lastgroup
		value = mo.group()
		column = mo.start() - line_start
		if kind == 'NUMBER':
			value = float(value) if '.' in value else int(value)
		elif kind == 'Identifier' and value in keywords:
			kind = value
		elif kind == 'NEWLINE':
			line_start = mo.end()
			line_num += 1
			continue
		elif kind == 'SKIP':
			continue
		elif kind == 'MISMATCH':
			raise RuntimeError(f'{value!r} unexpected on line {line_num}')
		yield Token(kind, value, line_num, column)


statements = '''

#include <iostream>
using namespace std;

int main() {
    
    double n1, n2, n3;

    cout << "Enter three numbers: ";
    cin >> n1 >> n2 >> n3;

    // check if n1 is the largest number
    if(n1 >= n2 && n1 >= n3)
        cout << "Largest number: " << n1;

    // check if n2 is the largest number
    else if(n2 >= n1 && n2 >= n3)
        cout << "Largest number: " << n2;
    
    // if neither n1 nor n2 are the largest, n3 is the largest
    else 
        cout << "Largest number: " << n3;
  
    return 0;
}

'''

for token in tokenize(statements):
    print(token)
