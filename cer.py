#coding:utf-8
import sys
import difflib
from difflib import SequenceMatcher

'''
usage: python cer.py [original_file.txt]  [target_file.txt]
'''


####関数定義##############################################################################################
#input:string rows(行番号), string origin_st(正解の文字列), string target_st(比較対象の文字列)
#return:num charas(語数),num diff_charas(異なる語数) 
def diffLines(rows, origin_st, target_st):
    
    s1=list(origin_st)
    s2=list(target_st)

    #s2の中で、s1と比較して異なる語のリスト
    diff=[]
    #語数
    num_charas=len(s1)
    #削除語
    num_delete=0
    #挿入後
    num_insert=0
    #置換後
    num_replace=0

    matcher = difflib.SequenceMatcher(None, s1, s2)
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == 'delete':
            diff.append('del'+''.join(s1[i1:i2]))
            num_delete+=i2-i1
            #print('delete',s1[i1:i2], i1, i2)
        elif tag == 'equal':
            pass
            #print('equal',i1, i2, j1, j2)
        elif tag == 'insert':
            diff.append('ins'+''.join(s2[j1:j2]))
            num_insert+=j2-j1
            #print('insert',s2[j1:j2], j1, j2, i1)
        elif tag == 'replace':
            diff.append('rep'+''.join(s1[i1:i2])+'->'+''.join(s2[j1:j2]))
            num_replace+=i2-i1
            #print('replace',s1[i1:i2], i1, i2, s2[j1:j2], j1, j2)

    print(str(rows)+"行目 origin:"+str1)
    print(str(rows)+"行目 target:"+str2)
    print(str(rows)+"行目 diff  :"+','.join(diff))
    print("文字数:"+str(num_charas) + \
            "  削除語,挿入後,置換後:"+str(num_delete)+","+str(num_insert)+","+str(num_replace)+ \
            "  文字誤り率:"+str((num_delete+num_insert+num_replace)/num_charas) \
            )
    return num_charas, (num_delete+num_insert+num_replace)

####実行前のチェック##############################################################################################
##コマンドライン引数のチェック
#コマンドの引数が仕様通り
if len(sys.argv) == 3:    
    if (".txt" in sys.argv[1]) and  (".txt" in sys.argv[2]):
        pass
    else:
        print("input_file extension does not match '.txt'")
        sys.exit()
#コマンドの引数が合わない場合は中断
else:
    print("usage: python cer.py [original_file.txt]  [target_file.txt]")
    sys.exit()

##ファイルの行数チェック
with open(sys.argv[1],'r') as f:
    lines1 = [s.strip() for s in f.readlines()]
    num_rows1=len(lines1)
with open(sys.argv[2],'r') as f:
    lines2 = [s.strip() for s in f.readlines()]
    num_rows2=len(lines2)

if num_rows1 != num_rows2:
    print("error: Number of lines is different [original_file.txt]  [target_file.txt]")
    sys.exit()


####メイン処理##############################################################################################
if __name__ == "__main__":
    
    #総語数
    total_chara=0
    #総誤り語数
    total_diff_chara=0

    for i in range(len(lines1)):
        str1=lines1[i]
        str2=lines2[i]
        num_charas, diff_charas = diffLines(i+1,str1,str2)

        #総語数と総誤り語数をカウントアップ
        total_chara+=num_charas
        total_diff_chara+=diff_charas

    ##最終的な出力
    print("#################################################################")
    print("総文字数:"+str(total_chara) + \
        "  総誤り文字数:"+str(total_diff_chara) + \
        "  文字誤り率:"+str(total_diff_chara/total_chara) \
        )

    

