function changeText(id) {
    const topic = document.getElementById(id);
    const main_text = document.getElementById('main_text');
    const text = document.getElementById('text');
    if (topic.id === 'layouts') {
        main_text.style.display = 'flex'
        main_text.innerHTML = '<p>The most commonly used layouts are the ANSI layout and ISO, stand for two different world’s standards organizations. ' +
            'ANSI stands for the American National Standards Institute, and ISO stands for the International Organization for Standardization. <br>' +
            'These are both keyboard layouts that describe the size and position of the keys. These differ from the more known logical layouts such as QWERTY, Colemac and Dvorak. ' +
            'ANSI and ISO keyboards differ in the size and orientation of the Enter key, Backslash, and Left Shift keys. <br>' +
            'Many mechanical keyboard users say that the keyboard layout really depends on the user, but there are benefits and disadvantages to using either layout.</p>' +
            '<img src="images/ansi_iso.png" alt="ANSI ISO">';
        }
    else if (topic.id === 'form_factor') {
        main_text.style.display = 'flex'
        main_text.innerHTML = '<h3>Full-size / 100%</h3>' +
            '<p>The most recognizable mechanical keyboard form factor is the full size. Chances are, when you are asked to picture a keyboard, this is the form factor you will think of. The full size form factor has around 104 keys in total, depending on the layout.</p>' +
            '<img src="images/100.png" alt="100">' +
            '<p>The main idea behind this form factor is that it leaves nothing out, which makes it a perfect candidate for those who don’t really know their preferences yet. You get dedicated access to everything a keyboard can offer, such as the arrow keys, function row and number pad.<br>' +
            'This form factor is a brilliant choice if you absolutely need a number pad (also known as the tenkeypad or numpad) and won’t consider a separate numpad for your late night online banking extravaganzas or your Excel work.</p>' +
            '<h3>TKL / Tenkeyless / 80%</h3>' +
            '<p>Tenkeyless is the first step down the form factor ladder, tossing the ol’ numpad for some space on your desk. The TKL form factor has 88 or so keys in total, depending on the layout.</p>' +
            '<img src = "images/tkl.png" alt = "TKL">' +
            '<p>Highly popular in the PC-gaming community, the tenkeyless form factor is usually the optimal trade-off between form and function. Especially useful if you need a large amount of space to use your mouse, or have to deal with a smaller desk. If you play a competitive first-person shooter game on a low mouse sensitivity, you’ll know what I’m getting at. <br>' +
            'The other advantage is that you can place the keyboard more ergonomically in front of you, rather than having to tuck it towards the left and type at an angle.</p>' +
            '<h3>75%</h3>' +
            '<p>The 75% form factor is a bit smaller and cramped than the tenkeyless, but comes with more or less the same functionality.</p>' +
            '<img src="images/75.png" alt="75"> ' +
            '<p>A very unpopular choice on the market, however very practical. The 75% form factor retains most of the functionality of a TKL, but crams the keys right next to each other, with no wasted space. If you have ever used a laptop keyboard, you should feel right at home with the 75% form factor. <br>' +
            'The most obvious disadvantage here is that finding keys in a large block with no spacing sometimes proves difficult.</p>' +
            '<h3>60%</h3>' +
            '<p>The 60% form factor removes anything right of the Enter key, as well as the function row. These functions are usually accessible by holding FN and pressing other keys. The 60% form factor has about 61 keys, depending on the layout.</p>' +
            '<img src="images/60.png" alt="60">' +
            '<p>By opting for a 60% form factor keyboard, you enter the world of minimalism and aesthetics, rather than pragmatism and functionality. This form factor is fantastic if you are looking to customize your mechanical keyboard, or just take it on the go with you. <br>' +
            'These are just some of the most common form factors, there are a lot more such as 106%, 65%, even down to 40% and custom form factors suited for very particular needs (looking at you, ctrl+c ctrl+c macropad).</p>' +
            '<img src="images/form_factor.jpg" alt="Form Factor">';
    }
    else if (topic.id === 'keycaps') {
        main_text.style.display = 'flex'
        main_text.innerHTML = '<h3>Keycaps</h3>' +
            '<p>Keycaps and keycap sets are a rabbit hole in and of itself.<br>' +
            'We have amazing metal caps from RAMA Works,</p>' +
            '<img src="images/rama.png" alt="rama">' +
            '<p>Fantastic pieces of resin art from the likes of Jelly Key,</p>' +
            '<img src="images/jelly.png" alt="jelly" ' +
            '<p>And full sets from renowed companies such as GMK.</p>' +
            '<img src="images/gmk.png" alt="gmk">' +
            '<p>But their manufacturer isn`t the only thing to take into consideration there are several profiles that affect the typing experience.</p>' +
            '<img src="images/keycap_profile.png" alt = "keycap">';
    }
    else if (topic.id === 'switches') {
        main_text.style.display = 'flex'
        main_text.innerHTML = '<p>But what is a keyboard without switches?<br>' +
            'Switches are the mechanical (hence mechanical keyboard) components that are responsible for actualy registering the user inputs.<br>' +
            'Some more known brands are Cherry, Kailh and Gateron</p>' +
            '<p>Some Cherry MX switches</p>' +
            '<img src="images/cherry.png" alt="cherry">' +
            '<p>Some Kailh switches</p>' +
            '<img src="images/kailh.png" alt="kailh">' +
            '<p>And some Gateron switches</p>' +
            '<img src="images/gateron.png" alt="gateron">' +
            '<p>They all have different ranges of switches, from linears to tactiles to clickys, that give different typing experiences and sound profiles. Some of these brands even have their own keycap compatibility, making finding sets and designing PCBs for these all switches a lot harder, sometimes impossible.<br>' +
            'It goes very in depth when it comes to switch specs, so I recommend researching to learn more.</p>' +
            '<p>We could even talk about the impact of lubing the switch, but that`s a topic for another time...</p>';
    }
    else if (topic.id === 'materials') {
        main_text.style.display = 'flex'
        main_text.innerHTML = '';
    }
    else if (topic.id === 'cables') {
        main_text.style.display = 'flex'
        main_text.innerHTML = '';
    }
}
