V_col_map = {
    'A': {'type': 'value', 'field': 'BRAND'},
    'B': {'type': 'value', 'field': 'DEFAULT_CODE'},
    'C': {'type': 'value', 'field': 'FULL_SIZE'},
    'D': {'type': 'value', 'field': 'LOAD_SPEED'},
    'E': {'type': 'value', 'field': 'MODEL'},
    'F': {'type': 'value', 'field': 'POSITION'},
    'G': {'type': 'value', 'field': 'PLY'},
    'H': {'type': 'value', 'field': 'CAT_FILTER'},
    'I': {'type': 'value', 'field': 'CALIFORNIA'},
    'J': {'type': 'value', 'field': 'PRICE'},
    'M': {'type': 'value', 'field': 'FET'},
    'P': {'type': 'value', 'field': 'WEIGHTS'},

    'L': {
        'type': 'formula',
        'field': '=(J{map_cell}*K{map_cell})+(K{map_cell}*M{map_cell})'
    },
    'O':{
        'type': 'formula',
        'field': '=P{map_cell}*K{map_cell}'
    },
}
VLK_col_map = {
    
    'CC': {'type': 'value', 'field': 'WEIGHTS'},

    'A': {'type': 'value', 'field': 'BRAND'},
    'B': {'type': 'value', 'field': 'DEFAULT_CODE'},
    'C': {'type': 'value', 'field': 'FULL_SIZE'},
    'D': {'type': 'value', 'field': 'LOAD_SPEED'},
    'E': {'type': 'value', 'field': 'MODEL'},
    'F': {'type': 'value', 'field': 'POSITION'},
    'G': {'type': 'value', 'field': 'PLY'},
    'H': {'type': 'value', 'field': 'CAT_FILTER'},

    # ---------------- CALIFORNIA ----------------
    'I': {'type': 'value', 'field': 'CALIFORNIA'},
    'J': {'type': 'value', 'field': 'PRICE'},
    'M': {'type': 'value', 'field': 'FET'},

    'L': {
        'type': 'formula',
        'field': '=(J{map_cell}*K{map_cell})+(K{map_cell}*M{map_cell})',
    },
    'O': {
        'type': 'formula',
        'field': '=CC{map_cell}*K{map_cell}'
    },

    # ---------------- LATROBE ----------------
    'Q': {'type': 'value', 'field': 'LATROBE'},
    'R': {'type': 'value', 'field': 'PRICE'},
    'U': {'type': 'value', 'field': 'FET'},

    'T': {
        'type': 'formula',
        'field': '=(S{map_cell}*R{map_cell})+(S{map_cell}*U{map_cell})',
        
    },
    'X': {
        'type': 'formula',
        'field': '=CC{map_cell}*S{map_cell}'
    },

    # ---------------- KENTUCKY ----------------
    'AC': {'type': 'value', 'field': 'KENTUCKY'},
    'AD': {'type': 'value', 'field': 'PRICE'},
    'AG': {'type': 'value', 'field': 'FET'},

    'AF': {
        'type': 'formula',
        'field': '=(AE{map_cell}*AD{map_cell})+(AE{map_cell}*AG{map_cell})',
        
    },
    'AI': {
        'type': 'formula',
        'field': '=CC{map_cell}*AE{map_cell}'
    },

    # ---------------- CARROLTON ----------------
    'AL': {'type': 'value', 'field': 'CARROLTON'},
    'AM': {'type': 'value', 'field': 'PRICE'},
    'AP': {'type': 'value', 'field': 'FET'},

    'AO': {
        'type': 'formula',
        'field': '=(AN{map_cell}*AM{map_cell})+(AN{map_cell}*AP{map_cell})',
        
    },
    'AR': {
        'type': 'formula',
        'field': '=CC{map_cell}*AN{map_cell}'
    },

    # ---------------- FORTWORTH ---------------- #
    'AU': {'type': 'value', 'field': 'FORTWORTH'},
    'AV': {'type': 'value', 'field': 'PRICE'},
    'AY': {'type': 'value', 'field': 'FET'},

    'AX': {
        'type': 'formula',
        'field': '=(AW{map_cell}*AV{map_cell})+(AW{map_cell}*AY{map_cell})',
        
    },
    'BB': {
        'type': 'formula',
        'field': '=CC{map_cell}*AW{map_cell}'
    },

    # ---------------- APOPKA ---------------- #
    'BC': {'type': 'value', 'field': 'APOPKA'},
    'BD': {'type': 'value', 'field': 'PRICE'},
    'BG': {'type': 'value', 'field': 'FET'},

    'BF': {
        'type': 'formula',
        'field': '=(BE{map_cell}*BD{map_cell})+(BE{map_cell}*BG{map_cell})',
        
    },
    'BJ': {
        'type': 'formula',
        'field': '=CC{map_cell}*BE{map_cell}'
    },


}

ps_LTL = {
    'A': {'type': 'value', 'field': 'BRAND'},
    'B': {'type': 'value', 'field': 'DEFAULT_CODE'},
    'C': {'type': 'value', 'field': 'FULL_SIZE'},
    'D': {'type': 'value', 'field': 'LOAD_SPEED'},
    'E': {'type': 'value', 'field': 'MODEL'},
    'F': {'type': 'value', 'field': 'POSITION'},
    'G': {'type': 'value', 'field': 'PLY'},

    # ----- CALIFORNIA ----- #
    'H': {'type': 'value', 'field': 'CALIFORNIA'},
    'L': {'type': 'value', 'field': 'PRICE'},
    'O': {'type': 'value', 'field': 'FET'},
    'N': {'type': 'formula', 
          'field': '=(L{map_cell}*M{map_cell})+(O{map_cell}*M{map_cell})'},

    # ----- LA TROBE ----- #
    'R': {'type': 'value', 'field': 'LATROBE'},
    'V': {'type': 'value', 'field': 'PRICE'},
    'Y': {'type': 'value', 'field': 'FET'},
    'X': {'type': 'formula', 
          'field': '=(V{map_cell}*W{map_cell})+(Y{map_cell}*W{map_cell})'},
    
    # ----- KENTUCKY ----- #
    'AC': {'type': 'value', 'field': 'KENTUCKY'},
    'AG': {'type': 'value', 'field': 'PRICE'},
    'AJ': {'type': 'value', 'field': 'FET'},
    'AI': {'type': 'formula', 
          'field': '=(AG{map_cell}*AH{map_cell})+(AJ{map_cell}*AH{map_cell})'},

    # ----- TEXAS ----- #
    'AM': {'type': 'value', 'field': 'CARROLTON'},
    'AN': {'type': 'value', 'field': 'PRICE'},
    'AQ': {'type': 'value', 'field': 'FET'},
    'AP': {'type': 'formula', 
          'field': '=(AN{map_cell}*AO{map_cell})+(AQ{map_cell}*AO{map_cell})'},
    
    # ----- Forthworth ----- #
    'AU': {'type': 'value', 'field': 'FORTWORTH'},
    'AV': {'type': 'value', 'field': 'PRICE'},
    'AY': {'type': 'value', 'field': 'FET'},
    'AX': {'type': 'formula', 
          'field': '=(AY{map_cell}*AW{map_cell})+(AV{map_cell}*AW{map_cell})'},
}

ps_TL = {
    # ------ Weights Computation ------ #
    'CC': {'type': 'value', 'field': 'WEIGHTS'},
    #California
    'BG': {'type': 'formula', 
          'field': '=(CC{map_cell}*AP{map_cell})'},
    #La Trobe
    'BH': {'type': 'formula', 
          'field': '=(CC{map_cell}*AE{map_cell})'},
    #Kentucky
    'BI': {'type': 'formula', 
          'field': '=(CC{map_cell}*T{map_cell})'},
    #Texas
    'BJ': {'type': 'formula', 
          'field': '=(CC{map_cell}*J{map_cell})'},
    #FORTWORTH
    'BK': {'type': 'formula', 
          'field': '=(CC{map_cell}*AZ{map_cell})'},

    'A': {'type': 'value', 'field': 'BRAND'},
    'B': {'type': 'value', 'field': 'DEFAULT_CODE'},
    'C': {'type': 'value', 'field': 'FULL_SIZE'},
    'D': {'type': 'value', 'field': 'LOAD_SPEED'},
    'E': {'type': 'value', 'field': 'MODEL'},
    'F': {'type': 'value', 'field': 'POSITION'},
    'G': {'type': 'value', 'field': 'PLY'},

    # ----- CALIFORNIA ----- #
    'H': {'type': 'value', 'field': 'CALIFORNIA'},
    'CB': {'type': 'value', 'field': 'PRICE'},
    # For computation of PS Trailer Loads
    'I': {'type': 'formula',
           'field': '=(CB{map_cell} - ROUND(CB{map_cell} * 0.1, 2))'},
    'O': {'type': 'value', 'field': 'FET'},
    'K': {'type': 'formula', 
          'field': '=(I{map_cell}*J{map_cell})+(O{map_cell}*J{map_cell})'},

    # ----- LA TROBE ----- #
    'R': {'type': 'value', 'field': 'LATROBE'},
    'CA': {'type': 'value', 'field': 'PRICE'},
    'S': {'type': 'formula',
           'field': '=(CA{map_cell} - ROUND(CA{map_cell} * 0.1, 2))'},
    'V': {'type': 'value', 'field': 'FET'},
    'U': {'type': 'formula', 
          'field': '=(S{map_cell}*T{map_cell})+(V{map_cell}*T{map_cell})'},
    
    # ----- KENTUCKY ----- #
    'AC': {'type': 'value', 'field': 'KENTUCKY'},
    'BZ': {'type': 'value', 'field': 'PRICE'},
    'AD': {'type': 'formula', 
           'field': '=(BZ{map_cell} - ROUND(BZ{map_cell} * 0.1, 2))'},
    'AG': {'type': 'value', 'field': 'FET'},
    'AF': {'type': 'formula', 
          'field': '=(AD{map_cell}*AE{map_cell})+(AG{map_cell}*AE{map_cell})'},
    
    # ----- TEXAS ----- #
    'AN': {'type': 'value', 'field': 'CARROLTON'},
    'BY': {'type': 'value', 'field': 'PRICE'},
    'AO': {'type': 'formula', 
           'field': '=(BY{map_cell} - ROUND(BY{map_cell} * 0.1, 2))'},
    'AR': {'type': 'value', 'field': 'FET'},
    'AQ': {'type': 'formula', 
          'field': '=(AO{map_cell}*AP{map_cell})+(AR{map_cell}*AP{map_cell})'},
    
    # ----- TEXAS ----- #

    'AX': {'type': 'value', 'field': 'FORTWORTH'},
    'AY': {'type': 'value', 'field': 'PRICE'},
    'CC': {'type': 'value', 'field': 'FET'},
    'BA': {'type': 'formula', 
          'field': '=(AY{map_cell}*AZ{map_cell})+(AZ{map_cell}*CC{map_cell})'},

}


Ware_gen_col_map = {
    
    'DA': {'type': 'value', 'field': 'WEIGHTS'},

    'A': {'type': 'value', 'field': 'BRAND'},
    'B': {'type': 'value', 'field': 'DEFAULT_CODE'},
    'C': {'type': 'value', 'field': 'FULL_SIZE'},
    'D': {'type': 'value', 'field': 'LOAD_SPEED'},
    'E': {'type': 'value', 'field': 'MODEL'},
    'F': {'type': 'value', 'field': 'POSITION'},
    'G': {'type': 'value', 'field': 'PLY'},
    'H': {'type': 'value', 'field': 'CAT_FILTER'},

    # ---------------- CALIFORNIA ----------------
    'I': {'type': 'value', 'field': 'CALIFORNIA'},
    'J': {'type': 'value', 'field': 'PRICE'},
    'M': {'type': 'value', 'field': 'FET'},

    'L': {
        'type': 'formula',
        'field': '=(J{map_cell}*K{map_cell})+(K{map_cell}*M{map_cell})',
    },
    'O': {
        'type': 'formula',
        'field': '=DA{map_cell}*K{map_cell}'
    },

    # ---------------- LATROBE ----------------
    'Q': {'type': 'value', 'field': 'LATROBE'},
    'R': {'type': 'value', 'field': 'PRICE'},
    'U': {'type': 'value', 'field': 'FET'},

    'T': {
        'type': 'formula',
        'field': '=(S{map_cell}*R{map_cell})+(S{map_cell}*U{map_cell})',
        
    },
    'X': {
        'type': 'formula',
        'field': '=DA{map_cell}*S{map_cell}'
    },

    # ---------------- KENTUCKY ----------------
    'AC': {'type': 'value', 'field': 'KENTUCKY'},
    'AD': {'type': 'value', 'field': 'PRICE'},
    'AG': {'type': 'value', 'field': 'FET'},

    'AF': {
        'type': 'formula',
        'field': '=(AE{map_cell}*AD{map_cell})+(AE{map_cell}*AG{map_cell})',
        
    },
    'AI': {
        'type': 'formula',
        'field': '=DA{map_cell}*AE{map_cell}'
    },

    # ---------------- CARROLTON ----------------
    'AL': {'type': 'value', 'field': 'CARROLTON'},
    'AM': {'type': 'value', 'field': 'PRICE'},
    'AP': {'type': 'value', 'field': 'FET'},

    'AO': {
        'type': 'formula',
        'field': '=(AN{map_cell}*AM{map_cell})+(AN{map_cell}*AP{map_cell})',
        
    },
    'AR': {
        'type': 'formula',
        'field': '=DA{map_cell}*AN{map_cell}'
    },

    # ---------------- FORTWORTH ---------------- #
    'AU': {'type': 'value', 'field': 'FORTWORTH'},
    'AV': {'type': 'value', 'field': 'PRICE'},
    'AY': {'type': 'value', 'field': 'FET'},

    'AX': {
        'type': 'formula',
        'field': '=(AW{map_cell}*AV{map_cell})+(AW{map_cell}*AY{map_cell})',
        
    },
    'BB': {
        'type': 'formula',
        'field': '=DA{map_cell}*AW{map_cell}'
    },

    # ---------------- APOPKA ---------------- #
    'BD': {'type': 'value', 'field': 'APOPKA'},
    'BE': {'type': 'value', 'field': 'PRICE'},
    'BH': {'type': 'value', 'field': 'FET'},

    'BG': {
        'type': 'formula',
        'field': '=(BF{map_cell}*BE{map_cell})+(BF{map_cell}*BH{map_cell})',
        
    },
    'BK': {
        'type': 'formula',
        'field': '=DA{map_cell}*BF{map_cell}'
    },

    # ---------------- WINCHESTER ---------------- #
    'BM': {'type': 'value', 'field': 'WINCHESTER'},
    'BN': {'type': 'value', 'field': 'PRICE'},
    'BQ': {'type': 'value', 'field': 'FET'},

    'BP': {
        'type': 'formula',
        'field': '=(BO{map_cell}*BN{map_cell})+(BO{map_cell}*BQ{map_cell})',
        
    },
    'BT': {
        'type': 'formula',
        'field': '=DA{map_cell}*BO{map_cell}'
    },

    # ---------------- MIAMI ---------------- #
    'BV': {'type': 'value', 'field': 'MIAMI'},
    'BW': {'type': 'value', 'field': 'PRICE'},
    'BZ': {'type': 'value', 'field': 'FET'},

    'BY': {
        'type': 'formula',
        'field': '=(BX{map_cell}*BW{map_cell})+(BX{map_cell}*BZ{map_cell})',
        
    },
    'CC': {
        'type': 'formula',
        'field': '=DA{map_cell}*BX{map_cell}'
    },

    # ---------------- BLOOMSBURG ---------------- #
    'CE': {'type': 'value', 'field': 'WINCHESTER'},
    'CF': {'type': 'value', 'field': 'PRICE'},
    'CI': {'type': 'value', 'field': 'FET'},

    'CH': {
        'type': 'formula',
        'field': '=(CG{map_cell}*CF{map_cell})+(CG{map_cell}*CI{map_cell})',
        
    },
    'CL': {
        'type': 'formula',
        'field': '=DA{map_cell}*CG{map_cell}'
    },

    # ---------------- TENNESSE ---------------- #
    'CN': {'type': 'value', 'field': 'TENNESSE'},
    'CO': {'type': 'value', 'field': 'PRICE'},
    'CR': {'type': 'value', 'field': 'FET'},

    'CQ': {
        'type': 'formula',
        'field': '=(CO{map_cell}*CP{map_cell})+(CR{map_cell}*CR{map_cell})',
        
    },
    'CU': {
        'type': 'formula',
        'field': '=DA{map_cell}*CP{map_cell}'
    },


}




