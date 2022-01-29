import asyncio
from pyppeteer.launcher import launch
from collections import Counter

# async def main(browser):
    # page = await browser.newPage()
    # await page.goto('http://example.com')
    # await page.screenshot({'path': 'example.png'})

    # dimensions = await page.evaluate('''() => {
        # return {
            # width: document.documentElement.clientWidth,
            # height: document.documentElement.clientHeight,
            # deviceScaleFactor: window.devicePixelRatio,
        # }
    # }''')

    # print(dimensions)

    # await browser.close()
    # >>> {'width': 800, 'height': 600, 'deviceScaleFactor': 1}

loop = asyncio.get_event_loop()
browser = launch(headless=False)
page = loop.run_until_complete(browser.newPage())


loop.run_until_complete(page.goto('http://127.0.0.1:8080/'))


# loop.run_until_complete(page.setViewport(
    # dict(width=300, height=480, isMobile=True, hasTouch=True)
# ))

# loop.run_until_complete(page.waitFor(5))


# loop.run_until_complete(page.waitFor(2))

# element = loop.run_until_complete(page.querySelector('.new-todo'))
# element = loop.run_until_complete(page.querySelector('.new-todo'))
# boundingBox = loop.run_until_complete(element.evaluate('''(element) => {
    # const bBox = element.getBoundingClientRect()
    # return {
      # x: bBox.x,
      # y: bBox.y,
      # width: bBox.width,
      # height: bBox.height
    # }
# }'''))
# # boundingBox = loop.run_until_complete(element.evaluate('(element) => element.getX()'))
# # boundingBox = loop.run_until_complete(page.evaluate("() => document.getElementsByClassName('items_list--item')[0].getBoundingClientRect().width"))
# print(boundingBox)

# loop.run_until_complete(element.tap())

elements = loop.run_until_complete(page.evaluate('''
    () => {
        function fullPath(el){
            var names = [];
            while (el.parentNode){
                if (el.id){
                    names.unshift('#'+el.id);
                    break;
                }else{
                    if (el==el.ownerDocument.documentElement) 
                        names.unshift(el.tagName.toLowerCase());
                    else{
                        for (var c=1,e=el;e.previousElementSibling;e=e.previousElementSibling,c++);
                        names.unshift(el.tagName.toLowerCase()+":nth-child("+c+")");
                    }
                    el=el.parentNode;
                }
            }
            return names.join(" > ");
        }

        var nodes = document.getElementsByClassName('mobile-content')[0].querySelectorAll("*")
        var elements = []
        nodes.forEach(function(v, _, _) {elements.push(v)})
        return elements.map((e) => {
            var bBox = e.getBoundingClientRect()
            return {
                element: e.localName,
                selector: fullPath(e),
                x: bBox.x,
                y: bBox.y,
                width: bBox.width,
                height: bBox.height
            }
        })
    }
'''))

viewport = loop.run_until_complete(page.evaluate('''
    () => {
        var e = document.getElementsByClassName('mobile-content')[0]
        var bBox = e.getBoundingClientRect()
        return {
            x: bBox.x,
            y: bBox.y,
            width: bBox.width,
            height: bBox.height
        }
    }
'''))

print(viewport)

# print(elements[0])


screen = loop.run_until_complete(page.screenshot())

from io import BytesIO
from PIL import Image
import numpy as np

img = np.array(Image.open(BytesIO(screen)))
viewport_img = img[60:540, 250:550]
Image.fromarray(viewport_img).show()
print(viewport_img.shape)


coverage = loop.run_until_complete(page.evaluate('() => {return window.__coverage__}'))

def file_coverage(statement_coverage):
    s = list(statement_coverage.values())
    cnt = Counter(s)
    stmts = sum(cnt.values())
    return (cnt[0], stmts)

def total_coverage(coverage):
    cov = [file_coverage(v['s']) for v in coverage.values()]

    not_covered = sum(n for n, _ in cov)
    all_stmts = sum(c for _, c in cov)
    return not_covered / all_stmts

print(total_coverage(coverage))
