import json
from http.server import BaseHTTPRequestHandler

marks_data = [{"name":"l3GovMS2Gb","marks":59},{"name":"efIeCVXqII","marks":98},{"name":"v","marks":77},{"name":"uv7g","marks":61},{"name":"XUAMOXpnw","marks":52},{"name":"G4EMjNBcI","marks":26},{"name":"niu","marks":65},{"name":"5O7","marks":58},{"name":"mIqX","marks":16},{"name":"2xHCSs","marks":95},{"name":"RSFhRcq","marks":12},{"name":"jac12M1dGY","marks":47},{"name":"yaWb","marks":68},{"name":"HM","marks":64},{"name":"s0o","marks":84},{"name":"wDib","marks":6},{"name":"0","marks":69},{"name":"7Qqnn","marks":50},{"name":"cYNMpLe","marks":28},{"name":"iduFdD","marks":27},{"name":"qw","marks":0},{"name":"6S12","marks":16},{"name":"hNf","marks":59},{"name":"n09PK8","marks":70},{"name":"Z7Yr4WAd","marks":77},{"name":"wJIQNU2Rm","marks":91},{"name":"GPW3UORj","marks":72},{"name":"Q","marks":12},{"name":"9ACnZC","marks":18},{"name":"58DcS","marks":25},{"name":"SR3","marks":10},{"name":"K00CfX","marks":3},{"name":"kWpmQZEn","marks":20},{"name":"E","marks":45},{"name":"gPoXsidACc","marks":77},{"name":"CdVIdOX","marks":43},{"name":"v81H7bl","marks":19},{"name":"wmObUkr1vv","marks":62},{"name":"2p","marks":5},{"name":"V3Lc","marks":29},{"name":"iV","marks":39},{"name":"iP16brX","marks":56},{"name":"cWEt0sm5s","marks":72},{"name":"Gl","marks":19},{"name":"mddr7jBktc","marks":14},{"name":"aQP6","marks":76},{"name":"bjJLVQG","marks":64},{"name":"dSzVHZEB7","marks":90},{"name":"nPjC","marks":67},{"name":"Q","marks":45},{"name":"M","marks":46},{"name":"Ubly","marks":4},{"name":"yZS8QX9tn","marks":65},{"name":"aG6As","marks":76},{"name":"xxvWxYWUAt","marks":61},{"name":"WfIo4KbZN","marks":85},{"name":"gHWj42DkeA","marks":43},{"name":"KGoveG6rK","marks":66},{"name":"C5bIVHCHL","marks":5},{"name":"cGbj5","marks":31},{"name":"c","marks":0},{"name":"8V8oU4MI3","marks":50},{"name":"TXkLX","marks":54},{"name":"Di36b","marks":84},{"name":"oA6C","marks":69},{"name":"EyQC1xd6","marks":39},{"name":"e5n","marks":99},{"name":"ZxdNL","marks":65},{"name":"HYkMjPs","marks":62},{"name":"T4SvcJp","marks":99},{"name":"pfceHawnxR","marks":21},{"name":"txJiGrdTY","marks":4},{"name":"23","marks":78},{"name":"i","marks":34},{"name":"Sgdfc","marks":20},{"name":"au23","marks":75},{"name":"IvBsIAe","marks":26},{"name":"9mFpy3","marks":73},{"name":"5AzGjoIv","marks":92},{"name":"q47iMIOddC","marks":47},{"name":"jxpf","marks":76},{"name":"89RMT8","marks":45},{"name":"P","marks":54},{"name":"IvRqPY","marks":69},{"name":"eR7rObtUL","marks":39},{"name":"cIWlKeEQe2","marks":10},{"name":"YE","marks":18},{"name":"Gdhk","marks":17},{"name":"tNiYGewqfc","marks":39},{"name":"B040","marks":48},{"name":"IAsyYGJI","marks":42},{"name":"neqi9W","marks":25},{"name":"W1lAd5al0T","marks":98},{"name":"rMK","marks":30},{"name":"JT1KM6tah","marks":60},{"name":"zf42","marks":72},{"name":"ts85","marks":36},{"name":"ll6CcMy","marks":8},{"name":"9T","marks":15},{"name":"JivxDW","marks":15}]

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        query_params = self.path.split('?')[-1].split('&')
        names = [param.split('=')[-1] for param in query_params if param.startswith('name=')]

        marks = []
        for name in names:
            student = next((item for item in marks_data if item["name"] == name), None)
            marks.append(student["marks"] if student else None)

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({"marks": marks}).encode('utf-8'))

        return

