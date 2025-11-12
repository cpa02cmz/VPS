import unittest
import os
import yaml

class TestIflowOrchestration(unittest.TestCase):
    
    def test_memory_file_exists(self):
        """Test that the memory file exists"""
        memory_path = os.path.join('.github', 'iflow', 'memory.md')
        self.assertTrue(os.path.exists(memory_path))
    
    def test_policies_files_exist(self):
        """Test that policy files exist"""
        policy_files = [
            'ci-optimization.md',
            'documentation.md',
            'innovation.md',
            'dependency-management.md'
        ]
        
        for policy_file in policy_files:
            policy_path = os.path.join('.github', 'iflow', 'policies', policy_file)
            self.assertTrue(os.path.exists(policy_path))
    
    def test_sandbox_files_exist(self):
        """Test that sandbox files exist"""
        sandbox_files = [
            'experimental-workflow.yml',
            'composite-action/action.yml',
            'benchmark-script.sh'
        ]
        
        for sandbox_file in sandbox_files:
            sandbox_path = os.path.join('.github', 'iflow', 'sandbox', sandbox_file)
            self.assertTrue(os.path.exists(sandbox_path))
    
    def test_experimental_workflow_structure(self):
        """Test that the experimental workflow has the correct structure"""
        workflow_path = os.path.join('.github', 'iflow', 'sandbox', 'experimental-workflow.yml')
        
        with open(workflow_path, 'r') as f:
            workflow = yaml.safe_load(f)
        
        # Check that it has the required keys
        self.assertIn('name', workflow)
        self.assertIn('on', workflow)
        self.assertIn('jobs', workflow)
        
        # Check that it has a test job
        self.assertIn('test', workflow['jobs'])

if __name__ == '__main__':
    unittest.main()