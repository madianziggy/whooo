# Intro reference edits — revision 10

Mode: built-in image edits using the supplied photographic compositions and approved WHOO artwork. Every image is a full-height background behind live app text and translucent controls. The final brief preserves the physical card poses exactly as in the original references: landscape cards standing on their sides, with printed art mapped to the card plane. Earlier interpretations that laid cards flat or widened their physical pose were discarded. These are reference-based raster edits, not pixel-identical originals.

| Step | Reference and role | Saved asset |
| --- | --- | --- |
| 1 | Original three-card graphite/silver/gold stack from `4c5bfbbe-e1c3-487a-a167-02ec478e5402(2).png`. Original on-its-side pose and reference chip; approved left-hand owl layout in neutral silver on graphite. | `/workspace/sites/whoo-card-mobile/dist/assets/intro-cards-fullscreen-v10.png` |
| 2 | Original phone/card pose from `images (15)(1).jpg`, with the approved opposite owl layout on shiny platinum and a glossy teal phone display. | `/workspace/sites/whoo-card-mobile/dist/assets/intro-wallet-phone-v10.png` |
| 3 | `9e19c097-0350-42b0-9f2b-6a957fc79d30(2).png`: exact supplied two-terminal composition, payment-ready mock screen on the black terminal, Revolut side text removed from the small white reader. | `/workspace/sites/whoo-card-mobile/dist/assets/intro-spending-terminal-v10.png` |

The original two approved owl layouts come from `WHOO CARD duo with owl artwork and tagline(2).png`. The phone/card composition moves to step two, while the payment-terminal artwork illustrates Start spending at step three. The terminal QR-style image is decorative artwork, with no payment action or new scan route. Existing wallet/deposit/funding behavior is preserved.

The header separately uses actual original pixels from `WHOO Card owl-eye dual mockup.png`, not another newly drawn owl. `/workspace/sites/whoo-card-mobile/dist/assets/whoo-approved-wordmark-v10.svg` embeds the source, crops x=234, y=230, width=472, height=224 on the 1774 × 887 image, and extracts teal ink onto transparency through an SVG colour matrix. The letter/eye geometry is not redrawn and there is no background tile. The transparent result was rendered and inspected.

Actual final sizes: `intro-cards-fullscreen-v10.png` 852 × 1847; `intro-wallet-phone-v10.png` 853 × 1844; `intro-spending-terminal-v10.png` 853 × 1844.

## Exact final prompt 1

Inputs, in order:

- `/workspace/scratch/fd20bfb23328/upload/4c5bfbbe-e1c3-487a-a167-02ec478e5402(2).png`
- `/workspace/scratch/fd20bfb23328/generated_images/exec-5c042a8d-dec7-484c-b7da-bd8eba4c948f.png`

Use case: precise compositing. IMAGE 1 IS THE EDIT TARGET AND ABSOLUTE POSE/COMPOSITION AUTHORITY: the tall full-height photo with three graphite/silver/gold bank cards standing upright ON THEIR SHORT SIDES in a perspective stack. IMAGE 2 is ONLY the approved monochrome WHOO printed FACE ART and metal-finish reference, NOT a pose reference. Restore and KEEP EXACTLY Image 1's original upright/on-its-side card geometry, orientation, positions, silhouette, thin edges, camera angle, three-card stack, original metallic chip position/shape/size/colour and dark full-height background. DO NOT lay any card flat, DO NOT add the platforms from Image 2, DO NOT widen or shorten any card, DO NOT move the cards. Change ONLY the printed artwork on the front card: replace Revolut Business lettering with the complete WHOO face artwork from Image 2: WHOO eye-wordmark and small CARD, huge cropped owl on the right half of the natural LANDSCAPE face, and 'Your money.' / 'Your business.' below the chip. Map that whole landscape artwork onto Image 1's card plane, ROTATED WITH THE CARD because the landscape card is standing on its side. The WHOO logo reads in the SAME rotated direction as the original Revolut Business lettering; do not print a portrait-layout card. Preserve Image 1's original chip absolutely unchanged. Keep graphite, silver/chrome artwork and the original silver/gold cards behind it. No teal card colour. Photographic microdetail, realistic reflections, flat printed ink without a thick raised logo. Keep the full portrait 9:19.5 canvas and generous upper negative space for live UI. No UI text or controls. This is only a surface-art edit of Image 1; all card poses stay exactly as supplied.

## Exact final prompt 2

Inputs, in order:

- `/workspace/scratch/fd20bfb23328/generated_images/exec-8f9cc49e-4287-4ac1-b389-24be78ae3aa3.png`
- `/workspace/scratch/fd20bfb23328/generated_images/exec-762daf78-a493-4631-bbab-540918f2c3d4.png`
- `/workspace/scratch/fd20bfb23328/upload/images (15)(1).jpg`

Use case: precise compositing. IMAGE 1 is the EDIT TARGET and its card/phone geometry is LOCKED: the tall full-screen phone-and-card photo with the bank card standing ON ITS SHORT SIDE, narrow/tall in the picture, against the lower front of the upright phone on concrete. IMAGE 2 is ONLY the accepted shiny PLATINUM card-face artwork and glossy TEAL screen-colour reference, not a pose reference. IMAGE 3 is the original Revolut pose and metallic-chip reference. Keep Image 1's EXACT card outer polygon, dimensions, original upright-on-its-side angle, position, phone silhouette, plinth, lighting, perspective and full 9:19.5 background. DO NOT turn the physical card to a new horizontal pose, do not lay it flat, do not widen it or reduce its height, do not move it. Only change its surface: map Image 2's complete silver/chrome LANDSCAPE WHOO face design onto that locked card plane, ROTATED NINETY DEGREES WITH THE CARD, because a normal landscape bank card is standing on its short side. Its whole WHOO/CARD logo, oversized dark owl artwork and 'Your money.' / 'Your business.' line must rotate together, the same orientation as the original Revolut card printing in Image 3, rather than being rearranged into a portrait design. Keep the original metallic Revolut-reference chip design and position from Image 3, not a black or coloured chip. Keep the shiny platinum/silver metal and dark owl shapes from Image 2. Recolour ONLY the blue phone display from Image 1 to the same glossy luminous teal glass gradient as Image 2. Phone hardware stays silver chrome. No other change, no newly invented scene, no UI or floating text, no border/dotted edge. The physical bank card stays exactly ON ITS SIDE as in Image 1 and Image 3.

## Exact final prompt 3

Inputs, in order:

- `/workspace/scratch/fd20bfb23328/upload/9e19c097-0350-42b0-9f2b-6a957fc79d30(2).png`

Use case: precise-object-edit. Edit this exact supplied photograph for a full-screen mobile 'Start spending' intro. Preserve the large black payment terminal and small white contactless reader, their precise shapes, original positions, camera angles, thin bevels, materials, stepped dark metal plinths, orange indicator lights, reflections and navy/charcoal backdrop. Make only two content edits: (1) On the existing dark glass touchscreen of the LARGE black terminal, add a realistic payment-ready screen mapped to that exact screen plane. It should look like a merchant terminal about to be scanned: a clean bright interface with a small 'Scan & pay' heading, '$25.00', a large crisp QR-code-style payment graphic, and a small 'Ready to pay' label. Keep it subtle, sharply rendered, with the original glass reflections and perspective, no hovering UI. (2) Remove the word 'Revolut' from the side of the SMALL WHITE reader, leaving clean plain white hardware, and remove any other Revolut branding. Do not replace it with WHOO or another logo. Do not change the small reader's contactless symbol. Extend only the upper navy/charcoal background upward into a tall 9:19.5 full-bleed portrait composition, with the upper 34 percent quiet negative space for live header/heading. The devices and continuous plinths occupy the lower two thirds and continue to the side and bottom edges. No extra devices, cards, coins, hands, graphics, frame, border, rounded image corners, app buttons or outside-the-terminal text. This remains the exact supplied photographic composition with a screen switched on and the competitor name removed.

