<script>
    import Header from './Header.svelte';
    import Footer from './Footer.svelte';
 
    let { children } = $props();
 </script>
 
 <div class="app">
    <Header />
 
    <div class="common-background">
    <main>
        {@render children()}
    </main>
    </div>
   
    <Footer />
 </div>