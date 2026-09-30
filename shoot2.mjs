import { chromium } from 'playwright-core';
const browser = await chromium.launch({ channel: 'chrome' });
const page = await browser.newPage({ viewport: { width: 1100, height: 1600 }, deviceScaleFactor: 2 });
await page.goto('http://localhost:8080/lodge/', { waitUntil: 'networkidle' });
await page.waitForTimeout(1200); // fonts + images
const shots = [['section.pursuits .sec-head', 'sechead']];
for (const [sel, name] of shots) {
  const el = page.locator(sel);
  await el.scrollIntoViewIfNeeded();
  await page.waitForTimeout(400);
  await el.screenshot({ path: `/tmp/${name}.jpg`, type: 'jpeg', quality: 88 });
  console.log('shot', name);
}
await browser.close();
