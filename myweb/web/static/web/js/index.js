/**
 * Created by fengxiaomai on 17/9/14.
 */

$(document).ready(function (){
    $(".line-operation").click(function (){
        $('html, body').animate({
            scrollTop: $(".menu_list").offset().top
        }, 500);
    });
});

var app = new Vue({
    el: '#app',
    data: {
        message: 'hello aaa'
    },
    methods: {
        reverseMessage: function () {
            this.message = this.message.split('').reverse().join('')
        }
    }
});

var app2 = new Vue({
    el: '#app-2',
    data: {
        message: '页面加载于' + new Date().toLocaleString()
    }
});

var app3 = new Vue({
    el: '#app-3',
    data: {
        seen: true
    }
});

var app4 = new Vue({
    el: '#app-4',
    data: {
       todos: [
           {text: 'wqfeqwf'},
           {text: 'wqrqwerq'},
           {text: 'qwrwvasdcv'}
       ]
    }
});

Vue.component('todo-item', {
    props: ['todo'],
    template: '<li>{{ todo.text }}</li>'
});

var app7 = new Vue({
    el: '#app-7',
    data: {
        groceryList: [
            {id: 0, text: 'qq'},
            {id: 1, text: 'ww'},
            {id: 2, text: 'ee'}
        ]
    }
});

