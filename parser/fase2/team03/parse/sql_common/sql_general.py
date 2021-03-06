from parse.ast_node import ASTNode
from jsonMode import showDatabases as showDB
from parse.symbol_table import SymbolTable


class ShowDatabases(ASTNode):
    def __init__(self, name, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.name = name
        self.graph_ref = graph_ref

    def execute(self, table: SymbolTable, tree):
        super().execute(table, tree)
        #result_name = self.name.execute(table, tree) #To not execute because we show data bases without filters
        return showDB()  # add filter using name_like_regex... this has to be stored on TS or comes from function?


class UseDatabase(ASTNode):
    def __init__(self, name, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.name = name
        self.graph_ref = graph_ref

    def execute(self, table: SymbolTable, tree):
        super().execute(table, tree)
        result_name = self.name.execute(table, tree)
        table.set_current_db(result_name)
        return "You are using \'" + str(result_name) + "\' DB"


class Union(ASTNode):
    def __init__(self, records_a, records_b, is_all, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.records_a = records_a
        self.records_b = records_b
        self.is_all = is_all
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        self.records_a = self.records_a.execute(table, tree)[1]
        self.records_b = self.records_b.execute(table, tree)[1]
        if self.is_all:
            return self.records_a + self.records_b
        else:
            in_first = set(self.records_a)
            in_second = set(self.records_b)
            in_second_but_not_in_first = in_second - in_first
            return self.records_a + list(in_second_but_not_in_first)


class Intersect(ASTNode):
    def __init__(self, records_a, records_b, is_all, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.records_a = records_a
        self.records_b = records_b
        self.is_all = is_all
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        self.records_a = self.records_a.execute(table, tree)[1]
        self.records_b = self.records_b.execute(table, tree)[1]
        inter_result = []
        for item_a in self.records_a:
            if item_a in self.records_b:
                inter_result.append(item_a)
        return inter_result


class Except(ASTNode):
    def __init__(self, records_a, records_b, is_all, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.records_a = records_a
        self.records_b = records_b
        self.is_all = is_all
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        self.records_a = self.records_a.execute(table, tree)[1]
        self.records_b = self.records_b.execute(table, tree)[1]
        if self.is_all:  # TODO I may have an idea of what the result
            inter_result = []
            for item_a in self.records_a:
                if item_a in self.records_b:
                    inter_result.append(item_a)
            complete_result = []
            for item_a in self.records_a:
                if item_a not in inter_result:
                    complete_result.append(item_a)
            for item_b in self.records_b:
                if item_b not in inter_result:
                    complete_result.append(item_b)
            return complete_result
        else:
            inter_result = []
            for item_a in self.records_a:
                if item_a not in self.records_b:
                    inter_result.append(item_a)
            return inter_result
