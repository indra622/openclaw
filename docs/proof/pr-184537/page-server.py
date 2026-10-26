from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from pathlib import Path
import json, threading, datetime
root=Path(__file__).resolve().parent / 'repro-output'
(root/'logs').mkdir(parents=True,exist_ok=True)
state={'title':'Article before switch','revision':0}
lock=threading.Lock()
html=b"""<!doctype html><html><head><meta charset="utf-8"><title>Article before switch</title><link rel="icon" href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR4nGP4z8DwHwAFAAH/iZk9HQAAAABJRU5ErkJggg=="><style>body{font:24px system-ui;padding:48px;background:#f8fafc;color:#172554}h1{font-size:36px}p{max-width:700px;line-height:1.5}.badge{background:#dbeafe;padding:12px;display:inline-block}</style></head><body><div class="badge">OpenClaw #183926 - local proof page</div><h1 id="title">Article before switch</h1><p>This harmless page changes its document title while the Dashboard is hidden.</p><p>No account, model call, personal message or external service is involved.</p><script>
let revision=-1;
async function refresh(){try{let s=await(await fetch('/state',{cache:'no-store'})).json();if(s.revision!==revision){revision=s.revision;document.title=s.title;document.querySelector('#title').textContent=s.title;await fetch('/ack',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({title:document.title,revision,visibility:document.visibilityState})});}}catch(e){}}
refresh();setInterval(refresh,500);
</script></body></html>"""
class H(BaseHTTPRequestHandler):
 def log_message(self,*args):pass
 def respond(self,data,mime):
  self.send_response(200);self.send_header('Content-Type',mime);self.send_header('Cache-Control','no-store');self.send_header('Content-Length',str(len(data)));self.end_headers();self.wfile.write(data)
 def do_GET(self):
  if self.path=='/state':
   with lock:b=json.dumps(state).encode()
   return self.respond(b,'application/json')
  return self.respond(html,'text/html; charset=utf-8')
 def do_POST(self):
  b=self.rfile.read(int(self.headers.get('Content-Length','0')))
  if self.path=='/update':
   with lock:state.update(title='Updated while native',revision=state['revision']+1)
  elif self.path=='/ack':
   d=json.loads(b);d['utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
   with (root/'logs/page-events.jsonl').open('a') as f:f.write(json.dumps(d)+'\n')
  self.respond(b'{}','application/json')
server=ThreadingHTTPServer(('127.0.0.1',0),H)
(root/'logs/page-server.json').write_text(json.dumps({'port':server.server_port,'url':'http://localhost:'+str(server.server_port)+'/article'}))
server.serve_forever()
