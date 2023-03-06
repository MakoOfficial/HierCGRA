def functions(): 
    return {
        "__INPUT__":  {"input": ["in0", ], "output": ["out0", ], "width": "32"}, 
        "__OUTPUT__": {"input": ["in0", ], "output": ["out0", ], "width": "32"}, 
        "__ADD__": {"input": ["in0", "in1"], "output": ["out0", ], "width": "32"}, 
        "__SUB__": {"input": ["in0", "in1"], "output": ["out0", ], "width": "32"}, 
        "__MUL__": {"input": ["in0", "in1"], "output": ["out0", ], "width": "32"}, 
        "__AND__": {"input": ["in0", "in1"], "output": ["out0", ], "width": "32"}, 
        "__OR__":  {"input": ["in0", "in1"], "output": ["out0", ], "width": "32"}, 
        "__XOR__": {"input": ["in0", "in1"], "output": ["out0", ], "width": "32"}, 
        "__NOT__": {"input": ["in0", ],      "output": ["out0", ], "width": "32"}, 
        "__LSHIFT__":  {"input": ["in0", "in1"], "output": ["out0", ], "width": "32"}, 
        "__RSHIFT__":  {"input": ["in0", "in1"], "output": ["out0", ], "width": "32"}, 
        "__MAD__":     {"input": ["in0", "in1", "in2"], "output": ["out0", ], "width": "32"}, 
        "__CONST__":   {"input": ["in0", ], "output": ["out0", ], "width": "32"}, 
        # "__REG__":     {"input": ["din", "ctr", ], "output": ["dout", ], "width": "32"}, 
        "__REG__":     {"input": ["in0", "in1", ], "output": ["out0", ], "width": "32"}, 
        # "__MEM__":  {"input": ["addr", "din", "ctr", ], "output": ["dout", ], "width": "32"}, 
        # "__MEM__":  {"input": ["in0", "in1", "in2", ], "output": ["out0", ], "width": "32"}, 
        # "__MEM__":  {"input": ["in0", ], "output": ["out0", ], "width": "32"}, 
        "__MEM__":  {"input": ["in0", "in1", ], "output": ["out0", ], "width": "32"}, 
        "__EQUAL__":   {"input": ["in0", "in1", ], "output": ["out0", ], "width": "32"}, 
        "__GREATER__": {"input": ["in0", "in1", ], "output": ["out0", ], "width": "32"}, 
        "__LESS__":    {"input": ["in0", "in1", ], "output": ["out0", ], "width": "32"}, 
        "__LOGICAND2__": {"input": ["in0", "in1", ], "output": ["out0", ], "width": "32"}, 
        "__LOGICAND3__": {"input": ["in0", "in1", "in2", ], "output": ["out0", ], "width": "32"}, 
        "__LOGICAND4__": {"input": ["in0", "in1", "in2", "in3", ], "output": ["out0", ], "width": "32"}, 
        "__LOGICOR2__": {"input": ["in0", "in1", ], "output": ["out0", ], "width": "32"}, 
        "__LOGICOR3__": {"input": ["in0", "in1", "in2", ], "output": ["out0", ], "width": "32"}, 
        "__LOGICOR4__": {"input": ["in0", "in1", "in2", "in3", ], "output": ["out0", ], "width": "32"}, 
        "__BRANCH2__": {"input": ["in0", ], "output": ["out0", "out1", ], "width": "32"}, 
        "__BRANCH3__": {"input": ["in0", ], "output": ["out0", "out1", "out2", ], "width": "32"}, 
        "__BRANCH4__": {"input": ["in0", ], "output": ["out0", "out1", "out2", "out3", ], "width": "32"}, 
        "__JOIN2__":   {"input": ["in0", "in1", "select"], "output": ["out0", ], "width": "32"}, 
        "__JOIN3__":   {"input": ["in0", "in1", "in2", "select"], "output": ["out0", ], "width": "32"}, 
        "__JOIN4__":   {"input": ["in0", "in1", "in2", "in3", "select"], "output": ["out0", ], "width": "32"}, 
        # "__ALU__": {"input": ["in0", "in1", "in2"], "output": ["out0", ], "width": "32"}, 
        "__ALU__": {"input": ["in0", "in1"], "output": ["out0", ], "width": "32"}, 
        "__INPUT__":  {"input": ["in0", ], "output": ["out0", ], "width": "32"}, 
        "__OUTPUT__":  {"input": ["in0", ], "output": ["out0", ], "width": "32"}, 
        "__DIV__":  {"input": ["in0", ], "output": ["out0", ], "width": "32"}, 
        "__IO__": {"input": ["in0", "in1"], "output": ["out0", ], "width": "32"}, 
    }

def units(): 
    return {
        "INPUT": {
            "input": ["in0", ], "output": ["out0", ], 
            "function": {"FUNC_INPUT0": "__INPUT__", }, 
            "pattern": {
                "__INPUT__": {"unit": ["FUNC_INPUT0", ], 
                    "port": {
                        "in0": "FUNC_INPUT0.in0", 
                        "out0": "FUNC_INPUT0.out0", 
                    }, 
                        "connection": [], 
                }, 
            }, 
            "compat": {}, 
        },
        "OUTPUT": {
            "input": ["in0", ], "output": ["out0", ], 
            "function": {"FUNC_OUTPUT0": "__OUTPUT__", }, 
            "pattern": {
                "__OUTPUT__": {"unit": ["FUNC_OUTPUT0", ], 
                    "port": {
                        "in0": "FUNC_OUTPUT0.in0", 
                        "out0": "FUNC_OUTPUT0.out0", 
                    }, 
                        "connection": [], 
                }, 
            }, 
            "compat": {}, 
        }, 
        "MEM": {
            "input": ["in0", "in1", "in2", ], "output": ["out0", ], 
            "function": {"FUNC_MEM0": "__MEM__", }, 
            "pattern": {
                "PATN_MEM0": {"unit": ["FUNC_MEM0", ], 
                    "port": {
                        "in0": "FUNC_MEM0.in0", 
                        "in1": "FUNC_MEM0.in1", 
                        "in2": "FUNC_MEM0.in2", 
                        "out0": "FUNC_MEM0.out0", 
                    }, 
                    "connection": [], 
                }, 
            }, 
            "compat": {}, 
        }, 
        # "MEM": {
        #     "input": ["in0", ], "output": ["out0", ], 
        #     "function": {"FUNC_MEM0": "__MEM__", }, 
        #     "pattern": {
        #         "PATN_MEM0": {"unit": ["FUNC_MEM0", ], 
        #             "port": {
        #                 "in0": "FUNC_MEM0.in0", 
        #                 "out0": "FUNC_MEM0.out0", 
        #             }, 
        #             "connection": [], 
        #         }, 
        #     }, 
        #     "compat": {}, 
        # }, 
        # "MEM": {
        #     "input": ["in0", "in1"], "output": ["out0", ], 
        #     "function": {"FUNC_MEM0": "__MEM__", }, 
        #     "pattern": {
        #         "PATN_MEM0": {"unit": ["FUNC_MEM0", ], 
        #             "port": {
        #                 "in0": "FUNC_MEM0.in0", 
        #                 "in1": "FUNC_MEM0.in1", 
        #                 "out0": "FUNC_MEM0.out0", 
        #             }, 
        #             "connection": [], 
        #         }, 
        #     }, 
        #     "compat": {}, 
        # },
        #  "ALU": {
        #     "input": ["in0", "in1", "in2", ], "output": ["out0", ], 
        #     "function": {"FUNC_ALU0": "__ALU__", }, 
        #     "pattern": {
        #         "PATN_ALU0": {"unit": ["FUNC_ALU0", ], 
        #             "port": {
        #                 "in0": "FUNC_ALU0.in0", 
        #                 "in1": "FUNC_ALU0.in1", 
        #                 "in2": "FUNC_ALU0.in2", 
        #                 "out0": "FUNC_ALU0.out0", 
        #             }, 
        #             "connection": [], 
        #         }, 
        #     }, 
        #     "compat": {}, 
        # },
        "ALU0": {
            "input": ["in0", "in1",], "output": ["out0", ], 
            "function": {"FUNC_ALU0": "__ALU__", }, 
            "pattern": {
                "PATN_ALU0": {"unit": ["FUNC_ALU0", ], 
                    "port": {
                        "in0": "FUNC_ALU0.in0", 
                        "in1": "FUNC_ALU0.in1", 
                        "out0": "FUNC_ALU0.out0", 
                    }, 
                    "connection": [], 
                }, 
            }, 
            "compat": {}, 
        },
        "ALU1": {
            "input": ["in0", "in1",], "output": ["out0", ], 
            "function": {"FUNC_ALU0": "__ALU__", }, 
            "pattern": {
                "PATN_ALU0": {"unit": ["FUNC_ALU0", ], 
                    "port": {
                        "in0": "FUNC_ALU0.in0", 
                        "in1": "FUNC_ALU0.in1", 
                        "out0": "FUNC_ALU0.out0", 
                    }, 
                    "connection": [], 
                }, 
            }, 
            "compat": {}, 
        },
        "ALU2": {
            "input": ["in0", "in1",], "output": ["out0", ], 
            "function": {"FUNC_ALU0": "__ALU__", }, 
            "pattern": {
                "PATN_ALU0": {"unit": ["FUNC_ALU0", ], 
                    "port": {
                        "in0": "FUNC_ALU0.in0", 
                        "in1": "FUNC_ALU0.in1", 
                        "out0": "FUNC_ALU0.out0", 
                    }, 
                    "connection": [], 
                }, 
            }, 
            "compat": {}, 
        },
        "IO": {
            "input": ["in0", "in1",], "output": ["out0", ], 
            "function": {"FUNC_ALU0": "__ALU__", }, 
            "pattern": {
                "PATN_ALU0": {"unit": ["FUNC_ALU0", ], 
                    "port": {
                        "in0": "FUNC_ALU0.in0", 
                        "in1": "FUNC_ALU0.in1", 
                        "out0": "FUNC_ALU0.out0", 
                    }, 
                    "connection": [], 
                }, 
            }, 
            "compat": {}, 
        },
        "ADD": {
            "input": ["in0", "in1",], "output": ["out0", ], 
            "function": {"FUNC_ADD0": "__ADD__", }, 
            "pattern": {
                "PATN_ADD0": {"unit": ["FUNC_ADD0", ], 
                    "port": {
                        "in0": "FUNC_ADD0.in0", 
                        "in1": "FUNC_ADD0.in1",  
                        "out0": "FUNC_ADD0.out0", 
                    }, 
                    "connection": [], 
                }, 
            }, 
            "compat": {}, 
        }, 
        "MUL": {
            "input": ["in0", "in1",], "output": ["out0", ], 
            "function": {"FUNC_MUL0": "__MUL__", }, 
            "pattern": {
                "PATN_MUL0": {"unit": ["FUNC_MUL0", ], 
                    "port": {
                        "in0": "FUNC_MUL0.in0", 
                        "in1": "FUNC_MUL0.in1",  
                        "out0": "FUNC_MUL0.out0", 
                    }, 
                    "connection": [], 
                }, 
            }, 
            "compat": {}, 
        }, 
        "SUB": {
            "input": ["in0", "in1",], "output": ["out0", ], 
            "function": {"FUNC_SUB0": "__SUB__", }, 
            "pattern": {
                "PATN_SUB0": {"unit": ["FUNC_SUB0", ], 
                    "port": {
                        "in0": "FUNC_SUB0.in0", 
                        "in1": "FUNC_SUB0.in1",  
                        "out0": "FUNC_SUB0.out0", 
                    }, 
                    "connection": [], 
                }, 
            }, 
            "compat": {}, 
        }, 
        "DIV": {
            "input": ["in0",], "output": ["out0", ], 
            "function": {"FUNC_DIV0": "__DIV__", }, 
            "pattern": {
                "PATN_DIV0": {"unit": ["FUNC_DIV0", ], 
                    "port": {
                        "in0": "FUNC_DIV0.in0",  
                        "out0": "FUNC_DIV0.out0", 
                    }, 
                    "connection": [], 
                }, 
            }, 
            "compat": {}, 
        }, 
    }

def switches(): 
    return {
        "FULLYCONN_1X1": {
            "input":  ["in0",], 
            "output": ["out0"], 
            "required": ["in0->out0"], 
            "graph": "", 
        }, 
        "FULLYCONN_1X2": {
            "input":  ["in0",], 
            "output": ["out0", "out1",], 
            "required": ["in0->out0", "in0->out1"], 
            "graph": "", 
        }, 
        "FULLYCONN_1X3": {
            "input":  ["in0",], 
            "output": ["out0", "out1", "out2",], 
            "required": ["in0->out0", "in0->out1", "in0->out2",], 
            "graph": "", 
        }, 
        "FULLYCONN_1X4": {
            "input":  ["in0",], 
            "output": ["out0", "out1", "out2", "out3"], 
            "required": ["in0->out0", "in0->out1", "in0->out2", "in0->out3",], 
            "graph": "", 
        }, 
        "FULLYCONN_2X1": {
            "input":  ["in0", "in1", ], 
            "output": ["out0", ], 
            "required": ["in0->out0", "in1->out0", ], 
            "graph": "", 
        }, 
        "FULLYCONN_4X1": {
            "input":  ["in0", "in1", "in2", "in3"], 
            "output": ["out0", ], 
            "required": ["in0->out0", "in1->out0", "in2->out0", "in3->out0", ], 
            "graph": "", 
        }, 
        "FULLYCONN_4X4": {
            "input":  ["in0", "in1", "in2", "in3"], 
            "output": ["out0", "out1", "out2", "out3"], 
            "required": ["in0->out0", "in0->out1", "in0->out2", "in0->out3", 
                         "in1->out0", "in1->out1", "in1->out2", "in1->out3", 
                         "in2->out0", "in2->out1", "in2->out2", "in2->out3", 
                         "in3->out0", "in3->out1", "in3->out2", "in3->out3", ], 
            "graph": "", 
        }, 
        "FULLYCONN_6X1": {
            "input":  ["in0", "in1", "in2", "in3", "in4", "in5", ], 
            "output": ["out0", ], 
            "required": ["in0->out0", "in1->out0", "in2->out0", "in3->out0", "in4->out0", "in5->out0", ], 
            "graph": "", 
        }, 
        "FULLYCONN_8X1": {
            "input":  ["in0", "in1", "in2", "in3", "in4", "in5", "in6", "in7"], 
            "output": ["out0", ], 
            "required": ["in0->out0", "in1->out0", "in2->out0", "in3->out0", 
                         "in4->out0", "in5->out0", "in6->out0", "in7->out0", ], 
            "graph": "", 
        }, 
        "FULLYCONN_8X4": {
            "input":  ["in0", "in1", "in2", "in3", "in4", "in5", "in6", "in7"], 
            "output": ["out0", "out1", "out2", "out3", ], 
            "required": ["in0->out0", "in0->out1", "in0->out2", "in0->out3", 
                         "in1->out0", "in1->out1", "in1->out2", "in1->out3", 
                         "in2->out0", "in2->out1", "in2->out2", "in2->out3", 
                         "in3->out0", "in3->out1", "in3->out2", "in3->out3", 
                         "in4->out0", "in4->out1", "in4->out2", "in4->out3", 
                         "in5->out0", "in5->out1", "in5->out2", "in5->out3", 
                         "in6->out0", "in6->out1", "in6->out2", "in6->out3", 
                         "in7->out0", "in7->out1", "in7->out2", "in7->out3", ], 
            "graph": "", 
        }, 
        "FULLYCONN_8X8": {
            "input":  ["in0", "in1", "in2", "in3", "in4", "in5", "in6", "in7"], 
            "output": ["out0", "out1", "out2", "out3", "out4", "out5", "out6", "out7"], 
            "required": ["in0->out0", "in0->out1", "in0->out2", "in0->out3", "in0->out4", "in0->out5", "in0->out6", "in0->out7", 
                         "in1->out0", "in1->out1", "in1->out2", "in1->out3", "in1->out4", "in1->out5", "in1->out6", "in1->out7", 
                         "in2->out0", "in2->out1", "in2->out2", "in2->out3", "in2->out4", "in2->out5", "in2->out6", "in2->out7", 
                         "in3->out0", "in3->out1", "in3->out2", "in3->out3", "in3->out4", "in3->out5", "in3->out6", "in3->out7", 
                         "in4->out0", "in4->out1", "in4->out2", "in4->out3", "in4->out4", "in4->out5", "in4->out6", "in4->out7", 
                         "in5->out0", "in5->out1", "in5->out2", "in5->out3", "in5->out4", "in5->out5", "in5->out6", "in5->out7", 
                         "in6->out0", "in6->out1", "in6->out2", "in6->out3", "in6->out4", "in6->out5", "in6->out6", "in6->out7", 
                         "in7->out0", "in7->out1", "in7->out2", "in7->out3", "in7->out4", "in7->out5", "in7->out6", "in7->out7", ], 
            "graph": "", 
        }, 
        "FULLYCONN_16X4": {
            "input":  ["in0", "in1", "in2", "in3", "in4", "in5", "in6", "in7", 
                       "in8", "in9", "in10", "in11", "in12", "in13", "in14", "in15", ], 
            "output": ["out0", "out1", "out2", "out3", ], 
            "required": ["in0->out0", "in0->out1", "in0->out2", "in0->out3", 
                         "in1->out0", "in1->out1", "in1->out2", "in1->out3", 
                         "in2->out0", "in2->out1", "in2->out2", "in2->out3", 
                         "in3->out0", "in3->out1", "in3->out2", "in3->out3", 
                         "in4->out0", "in4->out1", "in4->out2", "in4->out3", 
                         "in5->out0", "in5->out1", "in5->out2", "in5->out3", 
                         "in6->out0", "in6->out1", "in6->out2", "in6->out3", 
                         "in7->out0", "in7->out1", "in7->out2", "in7->out3", 
                         "in8->out0", "in8->out1", "in8->out2", "in8->out3", 
                         "in9->out0", "in9->out1", "in9->out2", "in9->out3", 
                         "in10->out0", "in10->out1", "in10->out2", "in10->out3", 
                         "in11->out0", "in11->out1", "in11->out2", "in11->out3", 
                         "in12->out0", "in12->out1", "in12->out2", "in12->out3", 
                         "in13->out0", "in13->out1", "in13->out2", "in13->out3", 
                         "in14->out0", "in14->out1", "in14->out2", "in14->out3", 
                         "in15->out0", "in15->out1", "in15->out2", "in15->out3", ], 
            "graph": "", 
        }, 
        "FULLYCONN_16X8": {
            "input":  ["in0", "in1", "in2", "in3", "in4", "in5", "in6", "in7", 
                       "in8", "in9", "in10", "in11", "in12", "in13", "in14", "in15", ], 
            "output": ["out0", "out1", "out2", "out3", "out4", "out5", "out6", "out7"], 
            "required": ["in0->out0", "in0->out1", "in0->out2", "in0->out3", "in0->out4", "in0->out5", "in0->out6", "in0->out7", 
                         "in1->out0", "in1->out1", "in1->out2", "in1->out3", "in1->out4", "in1->out5", "in1->out6", "in1->out7", 
                         "in2->out0", "in2->out1", "in2->out2", "in2->out3", "in2->out4", "in2->out5", "in2->out6", "in2->out7", 
                         "in3->out0", "in3->out1", "in3->out2", "in3->out3", "in3->out4", "in3->out5", "in3->out6", "in3->out7", 
                         "in4->out0", "in4->out1", "in4->out2", "in4->out3", "in4->out4", "in4->out5", "in4->out6", "in4->out7", 
                         "in5->out0", "in5->out1", "in5->out2", "in5->out3", "in5->out4", "in5->out5", "in5->out6", "in5->out7", 
                         "in6->out0", "in6->out1", "in6->out2", "in6->out3", "in6->out4", "in6->out5", "in6->out6", "in6->out7", 
                         "in7->out0", "in7->out1", "in7->out2", "in7->out3", "in7->out4", "in7->out5", "in7->out6", "in7->out7", 
                         "in8->out0", "in8->out1", "in8->out2", "in8->out3", "in8->out4", "in8->out5", "in8->out6", "in8->out7", 
                         "in9->out0", "in9->out1", "in9->out2", "in9->out3", "in9->out4", "in9->out5", "in9->out6", "in9->out7", 
                         "in10->out0", "in10->out1", "in10->out2", "in10->out3", "in10->out4", "in10->out5", "in10->out6", "in10->out7", 
                         "in11->out0", "in11->out1", "in11->out2", "in11->out3", "in11->out4", "in11->out5", "in11->out6", "in11->out7", 
                         "in12->out0", "in12->out1", "in12->out2", "in12->out3", "in12->out4", "in12->out5", "in12->out6", "in12->out7", 
                         "in13->out0", "in13->out1", "in13->out2", "in13->out3", "in13->out4", "in13->out5", "in13->out6", "in13->out7", 
                         "in14->out0", "in14->out1", "in14->out2", "in14->out3", "in14->out4", "in14->out5", "in14->out6", "in14->out7", 
                         "in15->out0", "in15->out1", "in15->out2", "in15->out3", "in15->out4", "in15->out5", "in15->out6", "in15->out7", ], 
            "graph": "", 
        }, 
        "FULLYCONN_32X32": {
            "input":  ["in0",  "in1",  "in2",  "in3",  "in4",  "in5",  "in6",  "in7", 
                       "in8",  "in9",  "in10", "in11", "in12", "in13", "in14", "in15", 
                       "in16", "in17", "in18", "in19", "in20", "in21", "in22", "in23", 
                       "in24", "in25", "in26", "in27", "in28", "in29", "in30", "in31", ], 
            "output": ["out0",  "out1",  "out2",  "out3",  "out4",  "out5",  "out6",  "out7", 
                       "out8",  "out9",  "out10", "out11", "out12", "out13", "out14", "out15", 
                       "out16", "out17", "out18", "out19", "out20", "out21", "out22", "out23", 
                       "out24", "out25", "out26", "out27", "out28", "out29", "out30", "out31", ], 
            "required": ["in0->out0", "in0->out1", "in0->out2", "in0->out3", "in0->out4", "in0->out5", "in0->out6", "in0->out7", "in0->out8", "in0->out9", "in0->out10", "in0->out11", "in0->out12", "in0->out13", "in0->out14", "in0->out15", "in0->out16", "in0->out17", "in0->out18", "in0->out19", "in0->out20", "in0->out21", "in0->out22", "in0->out23", "in0->out24", "in0->out25", "in0->out26", "in0->out27", "in0->out28", "in0->out29", "in0->out30", "in0->out31", 
                         "in1->out0", "in1->out1", "in1->out2", "in1->out3", "in1->out4", "in1->out5", "in1->out6", "in1->out7", "in1->out8", "in1->out9", "in1->out10", "in1->out11", "in1->out12", "in1->out13", "in1->out14", "in1->out15", "in1->out16", "in1->out17", "in1->out18", "in1->out19", "in1->out20", "in1->out21", "in1->out22", "in1->out23", "in1->out24", "in1->out25", "in1->out26", "in1->out27", "in1->out28", "in1->out29", "in1->out30", "in1->out31", 
                         "in2->out0", "in2->out1", "in2->out2", "in2->out3", "in2->out4", "in2->out5", "in2->out6", "in2->out7", "in2->out8", "in2->out9", "in2->out10", "in2->out11", "in2->out12", "in2->out13", "in2->out14", "in2->out15", "in2->out16", "in2->out17", "in2->out18", "in2->out19", "in2->out20", "in2->out21", "in2->out22", "in2->out23", "in2->out24", "in2->out25", "in2->out26", "in2->out27", "in2->out28", "in2->out29", "in2->out30", "in2->out31", 
                         "in3->out0", "in3->out1", "in3->out2", "in3->out3", "in3->out4", "in3->out5", "in3->out6", "in3->out7", "in3->out8", "in3->out9", "in3->out10", "in3->out11", "in3->out12", "in3->out13", "in3->out14", "in3->out15", "in3->out16", "in3->out17", "in3->out18", "in3->out19", "in3->out20", "in3->out21", "in3->out22", "in3->out23", "in3->out24", "in3->out25", "in3->out26", "in3->out27", "in3->out28", "in3->out29", "in3->out30", "in3->out31", 
                         "in4->out0", "in4->out1", "in4->out2", "in4->out3", "in4->out4", "in4->out5", "in4->out6", "in4->out7", "in4->out8", "in4->out9", "in4->out10", "in4->out11", "in4->out12", "in4->out13", "in4->out14", "in4->out15", "in4->out16", "in4->out17", "in4->out18", "in4->out19", "in4->out20", "in4->out21", "in4->out22", "in4->out23", "in4->out24", "in4->out25", "in4->out26", "in4->out27", "in4->out28", "in4->out29", "in4->out30", "in4->out31", 
                         "in5->out0", "in5->out1", "in5->out2", "in5->out3", "in5->out4", "in5->out5", "in5->out6", "in5->out7", "in5->out8", "in5->out9", "in5->out10", "in5->out11", "in5->out12", "in5->out13", "in5->out14", "in5->out15", "in5->out16", "in5->out17", "in5->out18", "in5->out19", "in5->out20", "in5->out21", "in5->out22", "in5->out23", "in5->out24", "in5->out25", "in5->out26", "in5->out27", "in5->out28", "in5->out29", "in5->out30", "in5->out31", 
                         "in6->out0", "in6->out1", "in6->out2", "in6->out3", "in6->out4", "in6->out5", "in6->out6", "in6->out7", "in6->out8", "in6->out9", "in6->out10", "in6->out11", "in6->out12", "in6->out13", "in6->out14", "in6->out15", "in6->out16", "in6->out17", "in6->out18", "in6->out19", "in6->out20", "in6->out21", "in6->out22", "in6->out23", "in6->out24", "in6->out25", "in6->out26", "in6->out27", "in6->out28", "in6->out29", "in6->out30", "in6->out31", 
                         "in7->out0", "in7->out1", "in7->out2", "in7->out3", "in7->out4", "in7->out5", "in7->out6", "in7->out7", "in7->out8", "in7->out9", "in7->out10", "in7->out11", "in7->out12", "in7->out13", "in7->out14", "in7->out15", "in7->out16", "in7->out17", "in7->out18", "in7->out19", "in7->out20", "in7->out21", "in7->out22", "in7->out23", "in7->out24", "in7->out25", "in7->out26", "in7->out27", "in7->out28", "in7->out29", "in7->out30", "in7->out31", 
                         "in8->out0", "in8->out1", "in8->out2", "in8->out3", "in8->out4", "in8->out5", "in8->out6", "in8->out7", "in8->out8", "in8->out9", "in8->out10", "in8->out11", "in8->out12", "in8->out13", "in8->out14", "in8->out15", "in8->out16", "in8->out17", "in8->out18", "in8->out19", "in8->out20", "in8->out21", "in8->out22", "in8->out23", "in8->out24", "in8->out25", "in8->out26", "in8->out27", "in8->out28", "in8->out29", "in8->out30", "in8->out31", 
                         "in9->out0", "in9->out1", "in9->out2", "in9->out3", "in9->out4", "in9->out5", "in9->out6", "in9->out7", "in9->out8", "in9->out9", "in9->out10", "in9->out11", "in9->out12", "in9->out13", "in9->out14", "in9->out15", "in9->out16", "in9->out17", "in9->out18", "in9->out19", "in9->out20", "in9->out21", "in9->out22", "in9->out23", "in9->out24", "in9->out25", "in9->out26", "in9->out27", "in9->out28", "in9->out29", "in9->out30", "in9->out31", 
                         "in10->out0", "in10->out1", "in10->out2", "in10->out3", "in10->out4", "in10->out5", "in10->out6", "in10->out7", "in10->out8", "in10->out9", "in10->out10", "in10->out11", "in10->out12", "in10->out13", "in10->out14", "in10->out15", "in10->out16", "in10->out17", "in10->out18", "in10->out19", "in10->out20", "in10->out21", "in10->out22", "in10->out23", "in10->out24", "in10->out25", "in10->out26", "in10->out27", "in10->out28", "in10->out29", "in10->out30", "in10->out31", 
                         "in11->out0", "in11->out1", "in11->out2", "in11->out3", "in11->out4", "in11->out5", "in11->out6", "in11->out7", "in11->out8", "in11->out9", "in11->out10", "in11->out11", "in11->out12", "in11->out13", "in11->out14", "in11->out15", "in11->out16", "in11->out17", "in11->out18", "in11->out19", "in11->out20", "in11->out21", "in11->out22", "in11->out23", "in11->out24", "in11->out25", "in11->out26", "in11->out27", "in11->out28", "in11->out29", "in11->out30", "in11->out31", 
                         "in12->out0", "in12->out1", "in12->out2", "in12->out3", "in12->out4", "in12->out5", "in12->out6", "in12->out7", "in12->out8", "in12->out9", "in12->out10", "in12->out11", "in12->out12", "in12->out13", "in12->out14", "in12->out15", "in12->out16", "in12->out17", "in12->out18", "in12->out19", "in12->out20", "in12->out21", "in12->out22", "in12->out23", "in12->out24", "in12->out25", "in12->out26", "in12->out27", "in12->out28", "in12->out29", "in12->out30", "in12->out31", 
                         "in13->out0", "in13->out1", "in13->out2", "in13->out3", "in13->out4", "in13->out5", "in13->out6", "in13->out7", "in13->out8", "in13->out9", "in13->out10", "in13->out11", "in13->out12", "in13->out13", "in13->out14", "in13->out15", "in13->out16", "in13->out17", "in13->out18", "in13->out19", "in13->out20", "in13->out21", "in13->out22", "in13->out23", "in13->out24", "in13->out25", "in13->out26", "in13->out27", "in13->out28", "in13->out29", "in13->out30", "in13->out31", 
                         "in14->out0", "in14->out1", "in14->out2", "in14->out3", "in14->out4", "in14->out5", "in14->out6", "in14->out7", "in14->out8", "in14->out9", "in14->out10", "in14->out11", "in14->out12", "in14->out13", "in14->out14", "in14->out15", "in14->out16", "in14->out17", "in14->out18", "in14->out19", "in14->out20", "in14->out21", "in14->out22", "in14->out23", "in14->out24", "in14->out25", "in14->out26", "in14->out27", "in14->out28", "in14->out29", "in14->out30", "in14->out31", 
                         "in15->out0", "in15->out1", "in15->out2", "in15->out3", "in15->out4", "in15->out5", "in15->out6", "in15->out7", "in15->out8", "in15->out9", "in15->out10", "in15->out11", "in15->out12", "in15->out13", "in15->out14", "in15->out15", "in15->out16", "in15->out17", "in15->out18", "in15->out19", "in15->out20", "in15->out21", "in15->out22", "in15->out23", "in15->out24", "in15->out25", "in15->out26", "in15->out27", "in15->out28", "in15->out29", "in15->out30", "in15->out31", 
                         "in16->out0", "in16->out1", "in16->out2", "in16->out3", "in16->out4", "in16->out5", "in16->out6", "in16->out7", "in16->out8", "in16->out9", "in16->out10", "in16->out11", "in16->out12", "in16->out13", "in16->out14", "in16->out15", "in16->out16", "in16->out17", "in16->out18", "in16->out19", "in16->out20", "in16->out21", "in16->out22", "in16->out23", "in16->out24", "in16->out25", "in16->out26", "in16->out27", "in16->out28", "in16->out29", "in16->out30", "in16->out31", 
                         "in17->out0", "in17->out1", "in17->out2", "in17->out3", "in17->out4", "in17->out5", "in17->out6", "in17->out7", "in17->out8", "in17->out9", "in17->out10", "in17->out11", "in17->out12", "in17->out13", "in17->out14", "in17->out15", "in17->out16", "in17->out17", "in17->out18", "in17->out19", "in17->out20", "in17->out21", "in17->out22", "in17->out23", "in17->out24", "in17->out25", "in17->out26", "in17->out27", "in17->out28", "in17->out29", "in17->out30", "in17->out31", 
                         "in18->out0", "in18->out1", "in18->out2", "in18->out3", "in18->out4", "in18->out5", "in18->out6", "in18->out7", "in18->out8", "in18->out9", "in18->out10", "in18->out11", "in18->out12", "in18->out13", "in18->out14", "in18->out15", "in18->out16", "in18->out17", "in18->out18", "in18->out19", "in18->out20", "in18->out21", "in18->out22", "in18->out23", "in18->out24", "in18->out25", "in18->out26", "in18->out27", "in18->out28", "in18->out29", "in18->out30", "in18->out31", 
                         "in19->out0", "in19->out1", "in19->out2", "in19->out3", "in19->out4", "in19->out5", "in19->out6", "in19->out7", "in19->out8", "in19->out9", "in19->out10", "in19->out11", "in19->out12", "in19->out13", "in19->out14", "in19->out15", "in19->out16", "in19->out17", "in19->out18", "in19->out19", "in19->out20", "in19->out21", "in19->out22", "in19->out23", "in19->out24", "in19->out25", "in19->out26", "in19->out27", "in19->out28", "in19->out29", "in19->out30", "in19->out31", 
                         "in20->out0", "in20->out1", "in20->out2", "in20->out3", "in20->out4", "in20->out5", "in20->out6", "in20->out7", "in20->out8", "in20->out9", "in20->out10", "in20->out11", "in20->out12", "in20->out13", "in20->out14", "in20->out15", "in20->out16", "in20->out17", "in20->out18", "in20->out19", "in20->out20", "in20->out21", "in20->out22", "in20->out23", "in20->out24", "in20->out25", "in20->out26", "in20->out27", "in20->out28", "in20->out29", "in20->out30", "in20->out31", 
                         "in21->out0", "in21->out1", "in21->out2", "in21->out3", "in21->out4", "in21->out5", "in21->out6", "in21->out7", "in21->out8", "in21->out9", "in21->out10", "in21->out11", "in21->out12", "in21->out13", "in21->out14", "in21->out15", "in21->out16", "in21->out17", "in21->out18", "in21->out19", "in21->out20", "in21->out21", "in21->out22", "in21->out23", "in21->out24", "in21->out25", "in21->out26", "in21->out27", "in21->out28", "in21->out29", "in21->out30", "in21->out31", 
                         "in22->out0", "in22->out1", "in22->out2", "in22->out3", "in22->out4", "in22->out5", "in22->out6", "in22->out7", "in22->out8", "in22->out9", "in22->out10", "in22->out11", "in22->out12", "in22->out13", "in22->out14", "in22->out15", "in22->out16", "in22->out17", "in22->out18", "in22->out19", "in22->out20", "in22->out21", "in22->out22", "in22->out23", "in22->out24", "in22->out25", "in22->out26", "in22->out27", "in22->out28", "in22->out29", "in22->out30", "in22->out31", 
                         "in23->out0", "in23->out1", "in23->out2", "in23->out3", "in23->out4", "in23->out5", "in23->out6", "in23->out7", "in23->out8", "in23->out9", "in23->out10", "in23->out11", "in23->out12", "in23->out13", "in23->out14", "in23->out15", "in23->out16", "in23->out17", "in23->out18", "in23->out19", "in23->out20", "in23->out21", "in23->out22", "in23->out23", "in23->out24", "in23->out25", "in23->out26", "in23->out27", "in23->out28", "in23->out29", "in23->out30", "in23->out31", 
                         "in24->out0", "in24->out1", "in24->out2", "in24->out3", "in24->out4", "in24->out5", "in24->out6", "in24->out7", "in24->out8", "in24->out9", "in24->out10", "in24->out11", "in24->out12", "in24->out13", "in24->out14", "in24->out15", "in24->out16", "in24->out17", "in24->out18", "in24->out19", "in24->out20", "in24->out21", "in24->out22", "in24->out23", "in24->out24", "in24->out25", "in24->out26", "in24->out27", "in24->out28", "in24->out29", "in24->out30", "in24->out31", 
                         "in25->out0", "in25->out1", "in25->out2", "in25->out3", "in25->out4", "in25->out5", "in25->out6", "in25->out7", "in25->out8", "in25->out9", "in25->out10", "in25->out11", "in25->out12", "in25->out13", "in25->out14", "in25->out15", "in25->out16", "in25->out17", "in25->out18", "in25->out19", "in25->out20", "in25->out21", "in25->out22", "in25->out23", "in25->out24", "in25->out25", "in25->out26", "in25->out27", "in25->out28", "in25->out29", "in25->out30", "in25->out31", 
                         "in26->out0", "in26->out1", "in26->out2", "in26->out3", "in26->out4", "in26->out5", "in26->out6", "in26->out7", "in26->out8", "in26->out9", "in26->out10", "in26->out11", "in26->out12", "in26->out13", "in26->out14", "in26->out15", "in26->out16", "in26->out17", "in26->out18", "in26->out19", "in26->out20", "in26->out21", "in26->out22", "in26->out23", "in26->out24", "in26->out25", "in26->out26", "in26->out27", "in26->out28", "in26->out29", "in26->out30", "in26->out31", 
                         "in27->out0", "in27->out1", "in27->out2", "in27->out3", "in27->out4", "in27->out5", "in27->out6", "in27->out7", "in27->out8", "in27->out9", "in27->out10", "in27->out11", "in27->out12", "in27->out13", "in27->out14", "in27->out15", "in27->out16", "in27->out17", "in27->out18", "in27->out19", "in27->out20", "in27->out21", "in27->out22", "in27->out23", "in27->out24", "in27->out25", "in27->out26", "in27->out27", "in27->out28", "in27->out29", "in27->out30", "in27->out31", 
                         "in28->out0", "in28->out1", "in28->out2", "in28->out3", "in28->out4", "in28->out5", "in28->out6", "in28->out7", "in28->out8", "in28->out9", "in28->out10", "in28->out11", "in28->out12", "in28->out13", "in28->out14", "in28->out15", "in28->out16", "in28->out17", "in28->out18", "in28->out19", "in28->out20", "in28->out21", "in28->out22", "in28->out23", "in28->out24", "in28->out25", "in28->out26", "in28->out27", "in28->out28", "in28->out29", "in28->out30", "in28->out31", 
                         "in29->out0", "in29->out1", "in29->out2", "in29->out3", "in29->out4", "in29->out5", "in29->out6", "in29->out7", "in29->out8", "in29->out9", "in29->out10", "in29->out11", "in29->out12", "in29->out13", "in29->out14", "in29->out15", "in29->out16", "in29->out17", "in29->out18", "in29->out19", "in29->out20", "in29->out21", "in29->out22", "in29->out23", "in29->out24", "in29->out25", "in29->out26", "in29->out27", "in29->out28", "in29->out29", "in29->out30", "in29->out31", 
                         "in30->out0", "in30->out1", "in30->out2", "in30->out3", "in30->out4", "in30->out5", "in30->out6", "in30->out7", "in30->out8", "in30->out9", "in30->out10", "in30->out11", "in30->out12", "in30->out13", "in30->out14", "in30->out15", "in30->out16", "in30->out17", "in30->out18", "in30->out19", "in30->out20", "in30->out21", "in30->out22", "in30->out23", "in30->out24", "in30->out25", "in30->out26", "in30->out27", "in30->out28", "in30->out29", "in30->out30", "in30->out31", 
                         "in31->out0", "in31->out1", "in31->out2", "in31->out3", "in31->out4", "in31->out5", "in31->out6", "in31->out7", "in31->out8", "in31->out9", "in31->out10", "in31->out11", "in31->out12", "in31->out13", "in31->out14", "in31->out15", "in31->out16", "in31->out17", "in31->out18", "in31->out19", "in31->out20", "in31->out21", "in31->out22", "in31->out23", "in31->out24", "in31->out25", "in31->out26", "in31->out27", "in31->out28", "in31->out29", "in31->out30", "in31->out31", 
                         ], 
            "graph": "", 
        }, 
    }


