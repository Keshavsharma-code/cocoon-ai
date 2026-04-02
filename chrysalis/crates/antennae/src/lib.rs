pub struct ToolManifest;
impl ToolManifest {
    pub fn get_tools() -> Vec<String> { vec!["read_file".into(), "write_file".into()] }
}
