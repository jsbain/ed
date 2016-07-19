# coding: utf-8
# ed  a proof of concept of using a javascript editor inside a webview
#  uses codemirror to provide a capable editor
#  lightly wrapped in a webview
#
import ui
import os


def edopen(sender):
    '''open the file named in the textbox, load into editor'''
    w = sender.superview['webview1']
    f = sender.superview['filename']
    try:
        with open(f.text) as f:
            w.eval_js('editor.setValue("{}");'.format(escapestr(f.read())))
    except (IOError):
        print('file not found')


def edsave(sender):
    '''save the editor content to file in filename textbox'''
    w = sender.superview['webview1']
    f = sender.superview['filename']
    try:
        with open(f.text, 'w') as out_file:
            out_file.write(w.eval_js('editor.getValue();'))
    except(IOError):
        print('could not save')


def escapestr(s):
    '''escape quotes, and newlines.  probably needs other things escaped too'''
    return s.replace('\n', '\\n').replace('"', '\\"').replace('\'', "\\'")

# main script

e = ui.load_view('ed')
e['filename'].autocapitalization_type = ui.AUTOCAPITALIZE_NONE
e['filename'].autocorrection_type = False
# srcname='ed.html'  #doesnt work in webview?.  but does in webbrowser...wth?
srcname = 'CodeMirror-master/demo/ed.html'
# print os.path.abspath(srcname)
w = e['webview1']
w.load_url(os.path.abspath(srcname))

e.present('panel')
